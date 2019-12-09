import random
import numpy as np
import matplotlib.pyplot as plt

QTDE_INDIVIDUOS = 10
CORTE = 2
PROBABILIDADE_MUTACAO = 0.05
FITNESS = 28
f = open("Log.txt","w")

def geraPosicoes():
    y = []
    verificador = [x for x in range(8)]
    while(len(y) < 8):
        item = random.choice(verificador)
        if item not in y:
            y.append(item)
    return y 

def zeraMatriz(tabuleiro):
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            tabuleiro[i][j] = 0

def imprimeRainhas(geracao):
    linhas = [x for x in range(8)]
    for i in range(8):
        colunas = [0 for x in range(8)]
        linhas[i] = colunas
    for i in range(QTDE_INDIVIDUOS):
        for j in range(8):
            linhas[geracao[i][j]][j] = j+1
        print("Indivíduo ",i)
        for i in range(len(linhas)):
            print(linhas[i])
        zeraMatriz(linhas)
    
def retornaIndividuo(geracao, linha):
    linhas = [0 for x in range(8)]
    for i in range(8):
        coluna = [0 for x in range(8)]
        linhas[i] = coluna
    for j in range(8):
        linhas[geracao[linha][j]][j] = j+1
    return linhas

def retornaChild(child):
    linhas = [0 for x in range(8)]
    for i in range(8):
        coluna = [0 for x in range(8)]
        linhas[i] = coluna
    for j in range(8):
        linhas[child[j]][j] = j+1
    return linhas

def imprimeGeracao(geracao):
    for i in range(QTDE_INDIVIDUOS):
        print(geracao[i])
    print("\n")

def fitness(individuo, geracao):
    confrontos = 0
    # geração[1º][2º] => primeiro índice é referente ao indivíduo/tabuleiro
    #                    segundo índice é referente a rainha
    for colunaDaRainha in range(8):
        linhaDaRainha = geracao[colunaDaRainha]
        
        aux = ["" for i in range(8)]
        for i in range(8):
            aux1 = ["" for i in range(8)]
            aux[i] = aux1
        for col in range(8): #coluna
            for lin in range(8): #linha
                if (col == colunaDaRainha and lin == linhaDaRainha):
                    aux[lin][col] = 'R'
                elif (col == colunaDaRainha):
                    aux[lin][col] = 'X'
                elif (lin == linhaDaRainha):
                    aux[lin][col] = 'X'
                # Diagonal segundária
                # soma a linha com a coluna corrente no FOR 
                # e verifica se o resultado se é igual a soma 
                # da coluna da rainha com a linha da rainha
                elif ( (col > colunaDaRainha and lin < linhaDaRainha) or ( col < colunaDaRainha and lin > linhaDaRainha ) ):      
                    if ((col+lin) == (colunaDaRainha+linhaDaRainha)):
                        aux[lin][col] = 'X'
                    else:
                        aux[lin][col] = ' '
                # Diagonal primária
                # subtrai a linha com a coluna corrente no FOR 
                # e verifica se o resultado se é igual a subtração 
                # da coluna da rainha com a linha da rainha
                elif ( ( col < colunaDaRainha and lin < linhaDaRainha) or ( col > colunaDaRainha and lin > linhaDaRainha) ): 
                    if ((col-lin) == (colunaDaRainha-linhaDaRainha)):
                        aux[lin][col] = 'X'
                    else:
                        aux[lin][col] = ' '
                else:
                    aux[lin][col] = ' '
        #print('Todas as posições que a rainha ',colunaDaRainha+1,' está atacando.')
        for i in range(8):    
            print(aux[i])
        for i in range(8):  
            for y in range(8):  
                if (individuo[i][y] != 0 and (y+1) == individuo[i][y]):
                    if (individuo[i][y] != colunaDaRainha+1 ):
                        print(individuo[i])
                    else:
                        print([0,0,0,0,0,0,0,0])
            for j in range(8):  
                
                # A sentença : individuo[i][j] != 0
                # verifica se o conteúdo do indivíduo na posição i,j é diferente de zero
                # pois se for diferente de zero significa que existe uma rainha na posição i, j
                
                # A sentença : (j+1) == individuo[i][j]
                # Verifica se o valor de j+1 é igual ao número da rainha encontrada na posição i, j 
                
                # A sentença : individuo[i][j] != colunaDaRainha+1 
                # Verifica se a rainha encontrada é diferente da rainha que está atacando 
                
                if ( (individuo[i][j] != 0 ) and ( (j+1) == individuo[i][j] ) and ( individuo[i][j] != colunaDaRainha+1 )):
                    if (aux[i][j] == 'X'):
                        confrontos += 1
                        print('Rainha ', colunaDaRainha+1,' ataca ', individuo[i][j])

        print("\n")
    print('Confrontos :', confrontos)
    print('Fitness Final :',FITNESS-(confrontos/2))
    return int(FITNESS - (confrontos/2))
        
def roleta(geracao):
    total = 0
    labels = [i for i in range(QTDE_INDIVIDUOS)]
    for i in range(len(labels)):
        labels[i] = ('Indivíduo '+str(i))
    for i in range(QTDE_INDIVIDUOS):
        total += geracao[i][8]
    porcentagem = [x for x in range(QTDE_INDIVIDUOS)]
    roleta = [x for x in range(QTDE_INDIVIDUOS)]
    for i in range(QTDE_INDIVIDUOS):
        porcentagem[i] = (geracao[i][8]/total)*100
        # 360º ====> 100% 
        # xº   ====> porcentagem[i]
        # xº * 100%  ====>  360 * porcentagem[i]
        # xº  ====>  (360 * porcentagem[i]) /100
        if i > 0:
            roleta[i] = (360 * porcentagem[i]) / 100 + (roleta[i-1]) 
        else:
            roleta[i] = (360 * porcentagem[i]) / 100 
    #Para gerar graficos descomentar as linhas abaixo
    #ax1 = plt.subplots()
    #ax1.pie(roleta,labels = labels, autopct ='%1.1f%%', shadow = True, startangle=90)
    #ax1.axis('equal')
    #plt.show()
    parent1, parent2 = None, None
    parent1 = random.randint(0,360)
    parent2 = random.randint(0,360)
    parent1Selecionado = 0
    parent2Selecionado = 0
    for i in range(QTDE_INDIVIDUOS):
        if ( (parent1 < roleta[i]) and ( parent1 > roleta[i-1] ) ):
            parent1Selecionado = i
        if ( (parent2 < roleta[i]) and ( parent2 > roleta[i-1] ) ):
            parent2Selecionado = i
    print("Parent 1: ",parent1Selecionado)
    print("Parent 2: ",parent2Selecionado)
    return parent1Selecionado, parent2Selecionado
