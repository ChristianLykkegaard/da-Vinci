#!/usr/local/bin/python
import os

for i in range(0, 2):
  os.system("makeindex DaVinci_main.nlo -s nomencl.ist -o DaVinci_main.nls")
  os.system("makeindex -s DaVinci_main.ist -t DaVinci_main.slg -o DaVinci_main.syi DaVinci_main.syg")
  os.system("pdflatex DaVinci_main.tex ")

print "Done!", "\n\n", "Christian, you did a good job!"

