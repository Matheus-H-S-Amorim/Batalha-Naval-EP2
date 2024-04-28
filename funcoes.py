from dados import * 

#Função que cria o mapa
def cria_mapa(N): 
    matriz = []
    linha = [] 

    i = 0 
    while i<N:
        linha.append(' ')
        i+=1

    i = 0
    while i<N:
        matriz.append(linha)
        i+=1 
        print(matriz)

    return matriz

# Verifica se acabou os N's do Mapa 
def foi_derrotado(matriz): 
    for linha in matriz: 
        for item in linha: 
            if item=="N": 
                return False 
    return True
