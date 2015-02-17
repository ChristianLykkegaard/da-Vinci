pdflatex DaVinci_main.tex
makeindex DaVinci_main.nlo -s formalia/nomencl.ist -o DaVinci_main.nls
pdflatex DaVinci_main.tex

pause
