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
 def torneio(participantes, k = 1, t = 2, rodadaNr = 1):
    # q = A quantidade de individúos na geração
    
    # k = Se o valor de k = 1, o método de torneio é dito determinístico, 
    # por selecionar sempre o melhor indivíduo da população
    # Obs.:deve ser um valor entre 0 e 1

    # t = Representa quantos indivíduos vão competir entre si

    q = len(participantes)

    if (q <= t):
        if q == 1:
            return 0
        else:
            return participantes
    
    # Prepara a estrutura das (q) competições que vão acontecer na rodada do torneio
    rodada = [i for i in range(q)]
    for i in range(q):
        rodada[i] = [a for a in range(t)]

    # Prepara a estrutura dos vencedores de cada competição
    vencedores = [0 for i in range(q)]
    for i in range(q):
        vencedores[i] = [0 for a in range(2)]

    # Define quais são os (t) indivíduos que vão competir entre si
    for i in range(q):
        for j in range(t):
            rodada[i][j] = random.randint(0,q-1)
    
    print(' ')
    print('Rodada nº:',rodadaNr)
    for i in range(q):
        print(rodada[i])

    print(' ')
    print('Resultado da rodada nº:',rodadaNr)
    for i in range(q):
        for j in range(t):
            individuo = rodada[i][j]
            if (rodadaNr > 1):
                fitness = participantes[individuo][1]  
            else:
                fitness = participantes[individuo][8]  
            if (k == 1): # determinístico = seleciona o melhor indivíduo da população
                print('individuo : ',individuo,' - fitness: ',fitness,' - quem esta ganhando:',vencedores[i][0],' seu fitness é: ',vencedores[i][1])
                if (fitness >= vencedores[i][1] ):
                    vencedores[i][0] = individuo
                    vencedores[i][1] = fitness
            if (k == 0): # não determinístico = seleciona o pior indivíduo da população
                if (fitness < vencedores[i][1]):
                    vencedores[i][0] = individuo
                    vencedores[i][1] = fitness 
        print(vencedores[i]) 
    
    print(' ')
    print('Os vencedores da rodada nº:',rodadaNr)
    
    proxFase = [-1 for i in range(q)]
    for i in range(q):
        proxFase[i] = [-1 for a in range(2)]

    for i in range(q):
        if ( vencedores[i] not in proxFase ):
            proxFase[i] = vencedores[i]

    for i in range(q):
        if ([-1,-1] in proxFase):
            proxFase.remove([-1,-1])

    for i in range(len(proxFase)):
        print(proxFase[i])

    rodadaNr += 1
    resultado = torneio(proxFase, k, t, rodadaNr)

    if (resultado == 0):
        return proxFase
    else:
        return resultado

def crossoverUniforme(geracao, parent1, parent2):
    child1 = [x for x in range(8)]
    child2 = [x for x in range(8)]
    for i in range(8):
        selecao = random.randint(0,1)
        if(selecao == 1):
            child1[i] = geracao[parent1][i]
            child2[i] = geracao[parent2][i]
        elif(selecao == 0):
            child1[i] = geracao[parent2][i]
            child2[i] = geracao[parent1][i]
    #gera um número aleatório float entre 0 e 1
    m = random.uniform(0,1)
    #verifica se o número gerado é menor que a probabilidade
    if(m < PROBABILIDADE_MUTACAO):
        #se verdadeiro realiza a mutação 
        child1 = mutacao(child1)
        child2 = mutacao(child2)
    
    return (child1, child2)

def crossoverUmPonto(geracao, parent1, parent2):
    #cria dois vetores que vao receber os valores dos pais
    child1 = [x for x in range(8)]
    child2 = [x for x in range(8)]
    i = 0
    while(i < CORTE):
        #de i ate o valor de corte definido os filhos recebem os primeiros valores
        child1[i] = geracao[parent1][i]
        child2[i] = geracao[parent2][i]
        i += 1
    while(i < 8):
        #i que agora é igual o valor de corte - 1 vai até 7 para os filhos receberem os últimos valores
        child1[i] = geracao[parent2][i]
        child2[i] = geracao[parent1][i]
        i += 1
    #gera um número aleatório float entre 0 e 1
    m = random.uniform(0,1)
    #verifica se o número gerado é menor que a probabilidade
    if(m < PROBABILIDADE_MUTACAO):
        #se verdadeiro realiza a mutação 
        child1 = mutacao(child1)
        child2 = mutacao(child2)
    
    return (child1, child2)

def mutacao(child):
    index = random.randint(0,7)
    child[index] = random.randint(0,7)
    return child


QTDE_INDIVIDUOS = int(input("Informe a quantidade de Individuos"))
f.write("Quantidade de individuos selecionados = "+ str(QTDE_INDIVIDUOS))
geracao = [x for x in range(QTDE_INDIVIDUOS)]
for i in range(QTDE_INDIVIDUOS):
    geracao[i] = geraPosicoes()
imprimeGeracao(geracao)
imprimeRainhas(geracao)
for i in range(QTDE_INDIVIDUOS):
    individuo = retornaIndividuo(geracao, i)
    fitness_individuo = fitness(individuo, geracao[i])
    geracao[i].append(fitness_individuo)
print("INDIVÍDUOS COM SEUS RESPECTIVOS FITNESS")
imprimeGeracao(geracao)
parent1, parent2 = roleta(geracao)
#child1, child2 = crossoverUmPonto(geracao,parent1,parent2)
#child = retornaChild(child1)
#fitness = fitness(child, child1)
child1, child2 = crossoverUniforme(geracao, parent1, parent2)
print(child1)
print(child2)
#torneio(geracao)

# Arquivo
# "x" - Create - cria o arquivo ee retorna mensagem de erro caso o arquivo exista
# "a" - Append - vai criar o arquivo caso o caminho especificado não exista
#       Vai escrever no final do arquivo
# "w" - Write - vai criar o arquivo caso o caminho especificado não exista 
#       Vai sobreescrever o conteudo do arquivo
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
