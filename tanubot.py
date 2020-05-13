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

    tanubot_table_fixer                         = False
    tanubot_caption_adder                       = False
    tanubot_caption                             = ""
    tanubot_short_caption                       = ""
    tanubot_figure                              = False
    tanubot_example                             = False
    tanubot_still_in_preamble                   = True
    tanubot_table_caption_only                  = False
    tanubot_table_next_line_is_title            = False
    tanubot_table_next_line_is_header           = False
    tanubot_waiting_for_additional_caption_line = False
    tanubot_expecting_short_caption             = False
    text_size                                   = ""

    for (index,line) in enumerate(lines):

        tanubot_skip_line                           = False

        if "hypertarget" in line and "chapter" in line:
            tanubot_still_in_preamble = False

        if "\\begin{document}" in line:
            tanubot_still_in_preamble = False
            tanubot_skip_line = True

        if "\\end{document}" in line:
            tanubot_skip_line = True

        if tanubot_still_in_preamble:
            tanubot_skip_line = True

        if (tanubot_waiting_for_additional_caption_line):
            tanubot_caption += line.replace('\\^{}','',1).replace('\n',' ')
            if (tanubot_caption.find('\\^{}') > 0):
                tanubot_caption = tanubot_caption[0:tanubot_caption.find('\\^{}')]
            if line.count("\\^{}")>0:
                tanubot_waiting_for_additional_caption_line = False
            tanubot_skip_line = True

        if (line.count("\\^{}\\^{}") == 1):
            tanubot_expecting_short_caption = True
            tanubot_short_caption = line[line.find("\\^{}""\\^{}")+2*len("\\^{}"):].replace('\n',' ')
            if "\\^{}" in tanubot_short_caption:
                tanubot_short_caption =tanubot_short_caption.replace("\\^{}",'')
                tanubot_expecting_short_caption = False
            tanubot_skip_line = True
        elif (tanubot_expecting_short_caption):
            tanubot_short_caption += line.replace('\n',' ')
            if "\\^{}" in tanubot_short_caption:
                tanubot_short_caption =tanubot_short_caption.replace("\\^{}",'')
                tanubot_expecting_short_caption = False
            tanubot_skip_line = True

        if "TANUBOT" in line.upper():
            print("EXECUTING TANUBOT COMMAND: %s" % line)

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
            elif ("FIX\_TABLE" in line or ("TANUBOT" in line and "CAPTION" in line)):

                if ("FIX\_TABLE" in line):
                    text_size=line.split('=')[1].split(" ")[0].replace('\n','')

                tanubot_table_fixer = True

                if ("CAPTION" in line):

                    if ("TANUBOT CAPTION" in line and not "FIX\_TABLE" in line):

                        expect_carrot                   = line.count("\\^{}") > 0

                        tanubot_caption=line[line.find("CAPTION"):]
                        tanubot_caption=tanubot_caption[tanubot_caption.find("=")+1:].replace('\\^{}','',1).replace('\n',' ')

                        tanubot_table_caption_only = True
                        if expect_carrot and tanubot_caption.count('\\^{}')==0:
                                tanubot_waiting_for_additional_caption_line = True
                                continue
                        else:
                            if (tanubot_caption.find('\\^{}') > 0):
                                tanubot_caption = tanubot_caption[0:tanubot_caption.find('\\^{}')]
                            tanubot_caption = tanubot_caption.replace('\\^{}','',1)
                    else:
                        tanubot_caption=line.split('=')[2].replace('\\^{}','',1).replace('\n',' ')
                        if tanubot_caption.count('\\^{}')==0:
                            tanubot_waiting_for_additional_caption_line = True
                            continue
                        else:
                            tanubot_caption=tanubot_caption.replace('\\^{}','',1)


            elif ("TANUBOT FIGURE" in line):
                tanubot_caption_adder = True
                tanubot_figure = True
                tanubot_caption = line.split('=')[1].replace('\n',' ').replace('\\^{}','',1)
                expect_carrot =line.count("\\^{}") > 0

                if expect_carrot and tanubot_caption.count('\\^{}')==0:
                        tanubot_waiting_for_additional_caption_line = True
                        continue
                else:
                        if (tanubot_caption.find('\\^{}') > 0):
                            tanubot_caption = tanubot_caption[0:tanubot_caption.find('\\^{}')]
                        tanubot_caption = tanubot_caption.replace('\\^{}','',1)

            elif ("TANUBOT EXAMPLE" in line):
                tanubot_caption_adder           = True
                tanubot_example                 = True
                tanubot_caption                 = line.split('=')[1].replace('\n',' ').replace('\\^{}','',1)
                expect_carrot                   = line.count("\\^{}") > 0

                if expect_carrot and tanubot_caption.count('\\^{}')==0:
                        tanubot_waiting_for_additional_caption_line = True
                        continue
                else:
                    tanubot_caption = tanubot_caption.replace('\\^{}','',1)

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
                    f.write("\\begin{%s}[H]\n" % fig_type)
                    f.write("\\vspace{1.5em}\n")
                    f.write("    \\centering\n")
                    if len(old)>0 and old[0] in line:
                        line = line.replace(old[0],new[0])
                        old.pop()
                        new.pop()
                    f.write(line)
                    if (tanubot_short_caption.replace(' ','')):
                        f.write("    \\caption[%s]{%s}\n" % (tanubot_short_caption, tanubot_caption))
                    else:
                        f.write("    \\caption{%s}\n" % tanubot_caption)
                    f.write("\\end{%s}" % fig_type)

                elif not "{center}" in line:
                    if (not tanubot_skip_line ):
                        f.write(line)

            if ("\\end{center}" in line):
                    tanubot_caption       = ""
                    tanubot_short_caption = ""
                    tanubot_figure        = False
                    tanubot_example       = False
                    tanubot_caption_adder = False

        elif (tanubot_table_fixer):
            if ("\\begin{tabular}" in line):

                if (not tanubot_table_caption_only):
                    f.write("\\begin{singlespace}\n")
                    cols = line.split("{")[2].replace('}','').replace("\n","")
                    cols_vline = "|"

                    for col in cols:
                        cols_vline += col + ""

                    cols_vline += "|"

                    f.write("\\begin{table}[H]\n")
                    f.write("\\centering\n")
                    f.write("\\%s\n" % text_size)
                    f.write("\\begin{tabular}{%s}\n" % cols_vline)
                else:
                    f.write("\\begin{table}[H]\n")
                    f.write("\\%s\n" % text_size)
                    f.write("\\centering\n")
                    if (not tanubot_skip_line ):
                        f.write(line)


            elif (tanubot_table_next_line_is_title or tanubot_table_next_line_is_header):
                if (not tanubot_table_caption_only):
                    if ("multicolumn" in line):
                        tanubot_table_next_line_is_header = True
                        s = line.replace("\n","").split(" & ")[1].replace("}{"," $ ").replace("}","").replace("\\","").replace("{"," $ ").split(" $ ")
                        f.write ("\\hline\n")
                        f.write ("{} & \\multicolumn{%s}{%s|}{\\textbf{%s}} \\\\\n" % (s[1],s[2],s[3]))
                        f.write ("\\hline\n")
                    else:
                        f.write ("\\hline\n")
                        line_split = line.replace("\\\\","").replace("\n","").split(" & ")
                        for field_index, field in enumerate(line_split):
                            f.write ("\\textbf{%s}" % field)
                            if (field_index<len(line_split)-1):
                                f.write (" & ")
                        f.write ("\\\\\n")
                        tanubot_table_next_line_is_header = False
                elif (not tanubot_skip_line ):
                        f.write (line)

                tanubot_table_next_line_is_title = False

            elif ("\\end{tabular}" in line):
                tanubot_table_next_line_is_header = False
                tanubot_table_next_line_is_title = False
                tanubot_table_fixer = False
                f.write("\\end{tabular}\n")
                if (tanubot_short_caption.replace(' ','')!=""):
                    f.write("\\caption[%s]{%s}\n" % (tanubot_short_caption, tanubot_caption))
                else:
                    f.write("\\caption{%s}\n" % tanubot_caption)
                f.write("\\end{table}\n")
                tanubot_caption = ""
                tanubot_short_caption = ""
                if (not tanubot_table_caption_only):
                    f.write("\\normalsize\n")
                    f.write("\\end{singlespace}\n")
            else:
                if ("toprule" in line):
                    tanubot_table_next_line_is_title = True
                elif (not tanubot_skip_line ):
                    f.write(line.replace("toprule", "hline").replace("midrule", "hline").replace("bottomrule", "hline"))

        elif len(old)>0 and old[0] in line:
            f.write(line.replace(old[0],new[0]))
            old.pop()
            new.pop()


        elif (not tanubot_skip_line ):
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
