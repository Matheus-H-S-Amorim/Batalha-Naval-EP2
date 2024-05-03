from dados import * 
import random 

#Função que cria o mapa
def cria_mapa(N): 
    matriz = []

    for i in range(N):
        linha = ['  .'] * N 
        matriz.append(linha)

    return matriz

# Verifica se acabou os N's do Mapa 
def foi_derrotado(matriz): 
    NN= poe_cor('green2','   ')

    for linha in matriz: 
        for item in linha: 
            if item==NN: 
                return False 
    return True 


# função que verifica se posição do navio é adequada para o mapa 
def posicao_suporta(mapa,blocos,linha,coluna,vh): 
    NN= poe_cor('green2','   ')
    # Verifica se navio ficará para fora do mapa    
    tam = len(mapa)
    if (coluna+blocos)>tam and vh=='h' or (linha+blocos)>tam and vh=='v': 
        return False 
    
    # Se navio for alocado horizontalmente
    if vh=='h':     
        for i in range(0,blocos): 
            if mapa[linha][coluna+i]==NN:
                return False 
    # Se navio for alocado verticalmente
    elif vh=='v':     
        for i in range(0,blocos): 
            if mapa[linha+i][coluna]==NN:
                print(i)
                return False 
        return True
    
    return True

# Funcao que aloca navios no mapa 
def aloca_navios(mapa,blocos): 
    N = len(mapa)
    NN= poe_cor('green2','   ')
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
            mapa[linhaS+i][colunaS+j]=NN
        
            n+=1 
    return mapa



# Mostra mapa na situacao atual 
def mostra_mapa(mapa,ALFABETO): 
    # printar letras em cima
    print("   ",end="")           #pra alinhar letras pra direita 
    for letra in ALFABETO: 
        print(letra+"    ",end="")
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
    print("   ",end="") #pra alinhar letras pra direita 
    for letra in ALFABETO: 
        print(letra+"    ",end="")
        if letra == "J": 
            break
    print("\n")
    return ""

# Preenche MAPA do JOGADOR   
def Preenche_MAPA_JOG(PAISES,Mapa_Jog,Mapa_PC_oculto,ALFABETO,pais_jogador,paisSorteado):
    NN = poe_cor('green2','   ')
    lista_blocos_JOG = []                                         # Cria lista de blocos/navios pro Jogador 
    lista_navios_JOG = []                          
    for navio,blocos in PAISES[pais_jogador].items():
        lista_blocos_JOG.append(blocos)
        lista_navios_JOG.append(navio)
    
        
    #Perguntar pro JOG onde quer por navios
    k = 0 
    for bloco_JOG in lista_blocos_JOG:
        print("alocar: {0} ({1} blocos)\n".format(lista_navios_JOG[k],lista_blocos_JOG[k]))     # Informa navio a ser alocado 
        
        letra_jog = input( "Informe a letra: ")
        letra_jog = letra_jog.upper()
        while letra_jog not in ALFABETO: 
            print("Resposta inválida. Digite uma Letra válida.")
            letra_jog = input( "Informe a letra: ")
            letra_jog = letra_jog.upper()

        letra_jog = ALFABETO.find(letra_jog)

        linha_jog = int(input( "Informe a linha: ")) - 1    

        vh_jog = input( "Informe a orientação[v/h]: ")

        while linha_jog not in range(0,10) or posicao_suporta(Mapa_Jog,bloco_JOG,linha_jog,letra_jog,vh_jog)==False:  
            print("Resposta inválida. Digite uma Linha válida.")
            linha_jog = int(input( "Informe a linha: ")) - 1    
            vh_jog = input( "Informe a orientação[v/h]: ")

        print("Navio alocado!\n")

        i = 0 
        j = 0 
        n = 0 
        while n<bloco_JOG: 
            if vh_jog=='v': 
                i = n 
            elif vh_jog=='h':
                j = n 
            Mapa_Jog[linha_jog+i][letra_jog+j]= NN
            
            n+=1 
        print('        COMPUTADOR - {0}'.format(paisSorteado))
        print(mostra_mapa(Mapa_PC_oculto, ALFABETO),"\n")

        print('        JOGADOR - {0}'.format(pais_jogador))
        print(mostra_mapa(Mapa_Jog, ALFABETO),"\n")
        
        k+=1 # para informar sempre o proximo navio da lista 
    print("\nTodos os navios foram alocados!")

    return ""



# Funcao que poe cores no texto 
def poe_cor(cor,texto): 
    string = CORES[cor]+texto+CORES['reset']
    return string 


# Funcao JOGADOR ataca COMPUTADOR 
def JOG_Ataca_PC(PAISES,Mapa_Jog,Mapa_PC_oculto,Mapa_PC,ALFABETO,pais_jogador,paisSorteado):
    NN= poe_cor('green2','   ')
    X = poe_cor('red2','   ')
    A = poe_cor('blue2','   ')
        
    #Perguntar pro JOG onde quer ATACAR
    print("Coordenadas do seu disparo")

    letra_jog = input( "Letra: ")
    letra_jog = letra_jog.upper()
    letra_jog = ALFABETO.find(letra_jog)

    linha_jog = int(input( "Linha: ")) - 1


    if Mapa_PC[linha_jog][letra_jog] ==NN:
        Mapa_PC_oculto[linha_jog][letra_jog] = X
        Mapa_PC[linha_jog][letra_jog] = X
        resultado = "BOOOOMM!!!\n"
    else: 
        Mapa_PC_oculto[linha_jog][letra_jog] = A
        Mapa_PC[linha_jog][letra_jog] = A
        resultado = "ÁGUA!\n"
    
    letra_jog = ALFABETO[letra_jog]
    coordenada =letra_jog + str(linha_jog+1)
    print("\nJogador ---->>>>   {0}     {1}".format(coordenada,resultado))

    print('        COMPUTADOR - {0}'.format(paisSorteado))
    print(mostra_mapa(Mapa_PC_oculto, ALFABETO))
 
    print('        JOGADOR - {0}'.format(pais_jogador))
    print(mostra_mapa(Mapa_Jog, ALFABETO))
        


    return ""




# Funcao COMPUTADOR ataca JOGADOR
def PC_Ataca_JOG(PAISES,Mapa_Jog,Mapa_PC_oculto,Mapa_PC,ALFABETO,pais_jogador,paisSorteado):
    N = len(Mapa_Jog)
    NN= poe_cor('green2','   ')
    X = poe_cor('red2','   ')
    A = poe_cor('blue2','   ')        

    #sorteia linha, coluna e orientacao
    linhaS = random.randint(0, N-1)
    colunaS = random.randint(0, N-1)
    vhS = random.choice(['h', 'v'])

    # Verifica se sorteio é coerente com dimensões do mapa e caso não refaz sorteio
    while posicao_suporta(Mapa_Jog,1,linhaS,colunaS,vhS)== False: 
        linhaS = random.randint(0, N-1)
        colunaS = random.randint(0, N-1)
        vhS = random.choice(['h', 'v'])

    if Mapa_Jog[linhaS][colunaS] == NN:
        Mapa_Jog[linhaS][colunaS] = X
        resultado = "BOOOOMM!!!\n"
    else: 
        Mapa_Jog[linhaS][colunaS] = A 
        resultado = "ÁGUA!\n"
    
    colunaS = ALFABETO[colunaS]
    coordenada = colunaS + str(linhaS+1)
    
    print("Computador ---->>>>   {0}     {1}".format(coordenada,resultado))

    print('        COMPUTADOR - {0}'.format(paisSorteado))
    print(mostra_mapa(Mapa_PC_oculto, ALFABETO))
    
    print('        JOGADOR - {0}'.format(pais_jogador))
    print(mostra_mapa(Mapa_Jog, ALFABETO))
    
        
   

    return ""