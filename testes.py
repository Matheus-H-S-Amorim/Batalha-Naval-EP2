from funcoes import * 
from dados import *

###### Testando execução ########

# Cria mapas para PC e JOGADOR
Mapa_PC = cria_mapa(10)
Mapa_Jog = cria_mapa(10)

#testando como vai ficar 
blocos = [1,2,3]
print(aloca_navios(Mapa_PC,blocos))
print("\n")

print("prog comecou")

# MAPA PC
def mostra_mapa(mapa,ALFABETO): 
    # printar letras em cima
    print("   ",end="")           #pra alinhar letras pra direita 
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
    print("   ",end="") #pra alinhar letras pra direita 
    for letra in ALFABETO: 
        print(letra+"  ",end="")
        if letra == "J": 
            break
    print("\n")
    return ""



print(mostra_mapa(Mapa_Jog,ALFABETO))



'''
## Print pro usuario do tamanho do navio atual e navios
x = 'torpedeiro'
y = 2 

# Próximo navio ### fazer mostrar proximo navio 
print('alocar: {0} ({1} blocos) '.format(x,y))
# Próximos navios 
print('próximos:',end="")
lista_prox_navios = status_navios(PAISES,pais_jogador)
for item in lista_prox_navios: 
    print(' ',item,end=",")
'''
