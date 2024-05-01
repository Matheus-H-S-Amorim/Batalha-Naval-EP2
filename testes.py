from funcoes import * 
from dados import *

###### Testando execução ########

# Cria mapas para PC e JOGADOR
Mapa_PC = cria_mapa(10)
Mapa_Jog = cria_mapa(10)

#testando como vai ficar 


print(aloca_navios(Mapa_PC,blocos))   # Fazer receber do dic de paises 
print("\n")

# Sorteando pais do Computador 
paisSorteado = random.choice(list(PAISES))

# Jogador escolhe numero de pais 
num_pais_jogador= int(input("Qual o número da nação da sua frota?: "))

# Transforma Dicionario de PAISES em lista 
lista_paises = list(PAISES)
pais_jogador = lista_paises[num_pais_jogador-1]


#EX
print('COMPUTADOR - {0}'.format(paisSorteado))
print(mostra_mapa(Mapa_PC,ALFABETO))

print('JOGADOR - {0}'.format(pais_jogador))
print(mostra_mapa(Mapa_Jog,ALFABETO))


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


# Preenche mapa do Jogador 
num = 2

while True: 
    linha_jog = int(input( "Informe a linha: "))
    letra_jog = int(input( "Informe a letra: "))
    vh_jog = input( "Informe a orientação[v/h]: ")
    i = 0 
    j = 0 
    n = 0 
    while n<num: 
        if vh_jog=='v': 
            i = n 
        elif vh_jog=='h':
            j = n 
        Mapa_Jog[linha_jog+i][letra_jog+j]='N'
        print(mostra_mapa(Mapa_Jog, ALFABETO))
        n+=1 
 
