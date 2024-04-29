from dados import * 

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
