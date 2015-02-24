makeindex DaVinci_main.nlo -s nomencl.ist -o DaVinci_main.nls
makeindex -s DaVinci_main.ist -t DaVinci_main.slg -o DaVinci_main.syi DaVinci_main.syg
makeindex -s DaVinci_main.ist -t DaVinci_main.glg -o DaVinci_main.gls DaVinci_main.glo
makeindex -s DaVinci_main.ist -t DaVinci_main.alg -o DaVinci_main.acr DaVinci_main.acn
