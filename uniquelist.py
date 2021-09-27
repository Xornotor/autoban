# Script pra eliminar nomes repetidos da banlist.
# Made by Xornotor
# Let's defeat this bots!

import numpy as np

rfile = open("banlist.txt", "r")
linhas = rfile.readlines()
rfile.close()

banlist = []

for linha in linhas: banlist.append(linha)

banlist = np.unique(np.array(banlist)).tolist()

wfile = open("uniquebanlist.txt", "w")
wfile.writelines(banlist)
wfile.close()
