#!/usr/local/bin/python
import os

for i in range(0, 2):
  os.system("makeindex -s DaVinci_main.ist -t DaVinci_main.slg -o DaVinci_main.syi DaVinci_main.syg")
  os.system("makeindex -s DaVinci_main.ist -t DaVinci_main.glg -o DaVinci_main.gls DaVinci_main.glo")
  os.system("makeindex -s DaVinci_main.ist -t DaVinci_main.alg -o DaVinci_main.acr DaVinci_main.acn")
  os.system("pdflatex DaVinci_main.tex ")

print "Done!", "\n\n", "Christian, you did a good job!"

