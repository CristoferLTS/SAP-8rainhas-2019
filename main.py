import random from randint

def geraPosicoes():

def imprimeTabuleiro(tabuleiro):
  for i in range(8):
    print(tabuleiro[i])

tabuleiro = []
for i in range(8):
  array = []
  for j in range(8):
    array.append(i)
  tabuleiro.append(array)
imprimeTabuleiro(tabuleiro)
