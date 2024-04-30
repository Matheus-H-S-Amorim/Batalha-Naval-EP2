from dados import * 
import random 

#Função que cria o mapa
def cria_mapa(N): 
    matriz = []

    for i in range(N):
        linha = [' '] * N 
        matriz.append(linha)

    return matriz

# Verifica se acabou os N's do Mapa 
def foi_derrotado(matriz): 
    for linha in matriz: 
        for item in linha: 
            if item=="N": 
                return False 
    return True 


# função que verifica se posição do navio é adequada para o mapa 
def posicao_suporta(mapa,blocos,linha,coluna,vh): 
    # Verifica se navio ficará para fora do mapa    
    tam = len(mapa)
    if (coluna+blocos)>tam and vh=='h' or (linha+blocos)>tam and vh=='v': 
        return False 
    
    # Se navio for alocado horizontalmente
    if vh=='h':     
        for i in range(0,blocos): 
            if mapa[linha][coluna+i]=='N':
                return False 
    # Se navio for alocado verticalmente
    elif vh=='v':     
        for i in range(0,blocos): 
            if mapa[linha+i][coluna]=='N':
                print(i)
                return False 
        return True
    
    return True

# Funcao que aloca navios no mapa 
def aloca_navios(mapa,blocos): 
    N = len(mapa)
    for num in blocos: 
        #sorteia linha, coluna e orientacao
        linhaS = random.randint(0, N-1)
        colunaS = random.randint(0, N-1)
        vhS = random.choice(['h', 'v'])
        # Verifica se sorteio é coerente com dimensões do mapa e caso não refaz sorteio
        while posicao_suporta(mapa,num,linhaS,colunaS,vhS)== False: 
            linhaS = random.randint(0, N-1)
            colunaS = random.randint(0, N-1)
            vhS = random.choice(['h', 'v'])
        #Preenche mapa com localizações e orientações sorteadas
        i = 0 
        j = 0 
        n = 0 
        while n<num: 
            if vhS=='v': 
                i = n 
            elif vhS=='h':
                j = n 
            mapa[linhaS+i][colunaS+j]='N'
        
            n+=1 
    return mapa


# Mostra próximos navios  ##### fazer primeiro item sumir a cada iteração
def status_navios(PAISES,pais_jogador): 
    lista = []
    for navio,blocos in PAISES[pais_jogador].items():
        lista.append(navio)
    return lista


# Mostra o mapa do Jogo 
def mostra_mapa(mapa,ALFABETO): 
    
    # printar letras em cima
    print("   ",end="")                        #pra alinhar letras pra direita 
    for letra in ALFABETO: 
        print(letra+"  ",end="")
        if letra == "J": 
            break
    print('\n',end="")

    #printar mapa do PC
    for i in range (len(mapa)): 
        print(str(i+1)," ", end="")
        for j in range(len(mapa)):
            print(mapa[i][j]," ",end="")
        print(str(i+1))

    # Printar letras embaixo
    print("   ",end="")                       #pra alinhar letras pra direita 
    for letra in ALFABETO: 
        print(letra+"  ",end="")
        if letra == "J": 
            break
    print("\n")
    return ""