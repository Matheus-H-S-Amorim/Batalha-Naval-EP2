from dados import * 
import random 
import time 
from funcoes import *




# Mensagem inicial do jogo
print(" ====================================\n"
    '|                                     |\n'
    '| Bem-vindo ao INSPER - Batalha Naval |\n'
    '|                                     |\n'
    ' =======   xxxxxxxxxxxxxxxxx   ======= \n')

time.sleep(2) # espera 2 segs
print('\nIniciando o Jogo!\n') 
time.sleep(3)     # espera 3 seg 

# Sorteando pais do Computador 
paisSorteado = random.choice(list(PAISES))


# Print do pais que Computador jogará com 
print("Computador está alocando os navios de guerra do país {0}...".format(paisSorteado))
print("Computador já está em posição de batalha")
time.sleep(3)     # espera 3 seg

# Printar dicionario de paises 
i = 1 
for pais,infos in PAISES.items(): 
    print(str(i)+":",pais)
    for navio,blocos in infos.items():
        print("  ",blocos,navio)
    print("")
    i+=1

# Jogador escolhe numero de pais 
num_pais_jogador= int(input("Qual o número da nação da sua frota?: "))

# Transforma Dicionario em lista 
lista_paises = list(PAISES)
pais_jogador = lista_paises[num_pais_jogador-1]

# Informa pais escolhido e instrui jogador a alocar seus navios 
print("Você escolheu a nação {0}".format(pais_jogador))
print("Agora é a sua vez de alocar os seus navios de guerra!")


###### Testando execução ########

# Cria mapa 
Mapa_PC = cria_mapa(10)
Mapa_Jog = cria_mapa(10)

#testando como vai ficar 
blocos = [1,2,3]
print(aloca_navios(Mapa_PC,blocos))

x = 'torpedeiro'
y = 2 

# Próximo navio ### fazer mostrar proximo navio 
print('alocar: {0} ({1} blocos) '.format(x,y))

# Próximos navios 
print('próximos:',end="")
lista_prox_navios = status_navios(PAISES)
for item in lista_prox_navios: 
    print(' ',item,end=",")

