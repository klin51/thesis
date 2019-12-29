from __future__ import unicode_literals
import io
import shutil
import tempfile
import sys

def run_tanubot (input_file_name, output_file_name):

    f = io.open (input_file_name, "r", newline='')
    lines = f.readlines()
    f.close()

    tempname = tempfile.mktemp();
    shutil.copy (input_file_name, tempname)

    tanubot_task_cnt = 0

    f = io.open (tempname, "w", newline='')

    old=[]
    new=[]

    tanubot_table_fixer               = False
    tanubot_caption_adder             = False
    tanubot_caption                   = ""
    tanubot_figure                    = False
    tanubot_example                   = False
    tanubot_still_in_preamble         = True
    tanubot_table_caption_only        = False
    tanubot_table_next_line_is_title  = False
    tanubot_table_next_line_is_header = False
    text_size                         = ""

    for (index,line) in enumerate(lines):

        if "\\begin{document}" in line:
            tanubot_still_in_preamble = False
            continue

        if tanubot_still_in_preamble:
            continue

        if "TANUBOT" in line.upper():
            if ("TANUBOT IMAGE\_WIDTH" in line):
                new_width=line.split('=')[1].replace('\n','')
                old.append("0.9\linewidth")
                new.append(new_width  + "\linewidth")
            elif ("TANUBOT IMAGE\_HEIGHT" in line):
                new_width=line.split('=')[1].replace('\n','')
                old.append("0.9\paperheight")
                new.append(new_width  + "\paperheight")
            elif ("TANUBOT ABS\_IMAGE\_WIDTH" in line):
                new_width=line.split('=')[1].replace('\n','')
                old.append("0.9\linewidth")
                new.append(new_width)
            elif ("TANUBOT ABS\_IMAGE\_HEIGHT" in line):
                new_width=line.split('=')[1].replace('\n','')
                old.append("0.9\paperheight")
                new.append(new_width)
            elif ("TANUBOT FIX\_TABLE" in line or ("TANUBOT" in line and "CAPTION" in line)):
                text_size=line.split('=')[1].split(" ")[0].replace('\n','')
                if (line.split('=')[1].split(" ")[1]=="CAPTION"):
                    tanubot_caption=line.split('=')[2].replace('\n','')
                elif (line.split('=')[0] == "TANUBOT CAPTION"):
                    tanubot_caption=line.split('=')[1].replace('\n','')
                    tanubot_table_caption_only = True

                tanubot_table_fixer = True

            elif ("TANUBOT FIGURE" in line):
                tanubot_caption_adder = True
                tanubot_figure = True
                tanubot_caption = line.split('=')[1].replace('\n','')
            elif ("TANUBOT EXAMPLE" in line):
                tanubot_caption_adder = True
                tanubot_example = True
                tanubot_caption = line.split('=')[1].replace('\n','')
            else:
                print("UNKNOWN TANUBOT COMMAND IN FILE:")
                print(input_file_name)
                print("ON LINE #" + str(index) + ":")
                print( line)
                break


        elif (tanubot_caption_adder):

            if (tanubot_figure or tanubot_example):

                fig_type = ""
                if (tanubot_figure):
                    fig_type="figure"
                if (tanubot_example):
                    fig_type="Example"


                if ("\\adjustimage" in line):
                    print ("TANUBOT ADDING CAPTION TO EXAMPLE")
                    f.write("\\begin{%s}[H]\n" % fig_type)
                    f.write("    \\begin{center}\n")
                    f.write(line)
                    f.write("    \\caption{%s}\n" % tanubot_caption)
                    f.write("    \\end{center}\n")
                    f.write("\\end{%s}\n" % fig_type)

                elif not "{center}" in line:
                    f.write(line)

            if ("\\end{center}" in line):
                    tanubot_caption       = ""
                    tanubot_figure        = False
                    tanubot_example       = False
                    tanubot_caption_adder = False

        elif (tanubot_table_fixer):
            if ("\\begin{tabular}" in line):

                if (not tanubot_table_caption_only):
                    f.write("\\begin{singlespace}\n")
                    f.write("\\%s\n" % text_size)
                    cols = line.split("{")[2].replace('}','').replace("\n","")
                    cols_vline = "|"

                    for col in cols:
                        cols_vline += col + "|"

                    f.write("\\centering\n")

                    f.write("\\begin{table}[H]\n")
                    f.write("\\begin{tabular}{%s}\n" % cols_vline)
                else:
                    f.write("\\begin{table}[H]\n")
                    f.write(line)


            elif (tanubot_table_next_line_is_title or tanubot_table_next_line_is_header):
                if (not tanubot_table_caption_only):
                    if ("multicolumn" in line):
                        tanubot_table_next_line_is_header = True
                        s = line.replace("\n","").split(" & ")[1].replace("}{"," $ ").replace("}","").replace("\\","").replace("{"," $ ").split(" $ ")
                        f.write ("{} & \\multicolumn{%s}{%s|}{\\textbf{%s}} \\\\\n" % (s[1],s[2],s[3]))
                        f.write ("\\hline\n")
                    else:
                        line_split = line.replace("\\\\","").replace("\n","").split(" & ")
                        for field_index, field in enumerate(line_split):
                            f.write ("\\textbf{%s}" % field)
                            if (field_index<len(line_split)-1):
                                f.write (" & ")
                        f.write ("\\\\\n")
                        tanubot_table_next_line_is_header = False
                else:
                        f.write (line)

                tanubot_table_next_line_is_title = False
                #f.write("\\hline\n")

            elif ("\\end{tabular}" in line):
                tanubot_table_next_line_is_header = False
                tanubot_table_next_line_is_title = False
                tanubot_table_fixer = False
                f.write("\\end{tabular}\n")
                f.write("\\caption{%s}\n" % tanubot_caption)
                f.write("\\end{table}\n")
                if (not tanubot_table_caption_only):
                    f.write("\\normalsize\n")
                    f.write("\\end{singlespace}\n")
            else:
                if ("toprule" in line):
                    tanubot_table_next_line_is_title = True
                f.write(line.replace("toprule", "hline").replace("midrule", "hline").replace("bottomrule", "hline"))

        elif len(old)>0 and old[0] in line:
            f.write(line.replace(old[0],new[0]))
            old.pop()
            new.pop()


        else:
            f.write(line)

    f.close()
    shutil.copy (tempname, output_file_name)

def main():
    if len(sys.argv)==2:
        run_tanubot (sys.argv[1], sys.argv[1])
    elif len(sys.argv)==3:
        run_tanubot (sys.argv[1], sys.argv[2])
    else:
        print("Usage: python3 tanubot.py <filename>")
        print("")
        print("Tanubot can parse commands:")
        print("    TANUBOT IMAGE_WIDTH      = <width>    -- image width as a fraction of line width")
        print("    TANUBOT IMAGE_HEIGHT     = <height>   -- image height as a fraction of paper height")
        print("    TANUBOT ABS_IMAGE_WIDTH  = <widthcm>  -- image width, max in cm, e.g. 7cm")
        print("    TANUBOT ABS_IMAGE_HEIGHT = <heightcm> -- image height, max in cm, e.g. 7cm")
        print("")
        print("Insert these into a cell preceeding the image(s) to be resized. Multiple commands can be put into one cell and they will act on subsequent images.")

if __name__ == '__main__':
    main()
