FILE=main
LATEX=latexmk -g -e '$$pdflatex=q/pdflatex %O -shell-escape %S/' -pdf

MAKE_PRETTY = perl -p -e 's/ugly.tex/pretty.tex/g' $(FILE).tex > $(FILE)_pretty.tex
MAKE_UGLY   = perl -p -e 's/pretty.tex/ugly.tex/g' $(FILE).tex > $(FILE)_ugly.tex

.PHONY: all clean

all: latex pdf

pdf: pretty ugly

clean:
	$(LATEX) -C *.tex
	find . -name "*.texn" -delete
	find . -name "*.aux" -delete
	find . -name __pycache__ -delete
	find . -name temperament.tex -delete
	find . -name intro.tex -delete
	find . -name "*conflicted copy*" -exec rm {} \;
	rm -rf "_minted-*"
	rm -rf methods_files
	rm -rf analysis_1_files
	rm -rf analysis_2_files
	rm -rf analysis_3_files

latex:
	#find . -name *.ipynb -exec jupyter-nbconvert --template noprompt {} --to hide_code_latex \;
	find . -maxdepth 1 -name "*.ipynb" -exec jupyter-nbconvert {} --to hide_code_latex \;

	echo "trimming empty verbatim environments"
	find . -maxdepth 1 -name "*.tex" -exec sed -in '/\\begin{Verbatim}/ { N; /\\begin{Verbatim}\[commandchars=\\\\\\{\\}]\n$$/ { N; /\\end{Verbatim}/ { d; } ; } ; }' {} \;
	echo "trimming hspaces"
	find . -maxdepth 1 -name "*.tex" -exec sed -in '/{ \\hspace\*{\\fill} \\\\}/d' {} \;
	echo "trimming empty lines at ends of verbatims"
	find . -maxdepth 1 -name "*.tex" -exec sed -in '/^$$/ { N; /\\end{Verbatim}/ { s/\n// ; } ; }' {} \;
	echo "trimming extra maketitles"
	find . -maxdepth 1 -name "*.tex" -exec sed -in '/\\maketitle/d' {} \;
	echo "trimming \\/"
	find . -maxdepth 1 -name "*.tex" -exec sed -in 's/\\\///g' {} \;

	python3 tanubot.py acknowledgements.tex
	python3 tanubot.py abstract.tex
	python3 tanubot.py methods.tex
	python3 tanubot.py analysis_1.tex
	python3 tanubot.py analysis_2.tex
	python3 tanubot.py analysis_3.tex
	python3 tanubot.py intro.tex
	python3 tanubot.py temperament.tex
	python3 tanubot.py conclusions.tex

	perl -00pe0 methods.tex
	perl -00pe0 analysis_1.tex
	perl -00pe0 analysis_2.tex
	perl -00pe0 analysis_3.tex
	perl -00pe0 intro.tex
	perl -00pe0 temperament.tex
	perl -00pe0 conclusions.tex

	perl -i -pe 's/\\end\{figure\}[\n\r\t\s]+/\\end\{figure\}/smg' methods.tex
	perl -i -pe 's/\\end\{figure\}[\n\r\t\s]+/\\end\{figure\}/smg' analysis_1.tex
	perl -i -pe 's/\\end\{figure\}[\n\r\t\s]+/\\end\{figure\}/smg' analysis_2.tex
	perl -i -pe 's/\\end\{figure\}[\n\r\t\s]+/\\end\{figure\}/smg' analysis_3.tex
	perl -i -pe 's/\\end\{figure\}[\n\r\t\s]+/\\end\{figure\}/smg' intro.tex
	perl -i -pe 's/\\end\{figure\}[\n\r\t\s]+/\\end\{figure\}/smg' temperament.tex
	perl -i -pe 's/\\end\{figure\}[\n\r\t\s]+/\\end\{figure\}/smg' conclusions.tex


pretty:
	$(MAKE_PRETTY)
	$(LATEX) $(FILE)_pretty.tex

ugly:
	$(MAKE_UGLY)
	$(LATEX) $(FILE)_ugly.tex
