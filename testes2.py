from funcoes import * 
from dados import *
import time 

# Cria mapas para PC e JOGADOR
Mapa_PC = cria_mapa(10)
Mapa_Jog = cria_mapa(10)

# tempo de espera
t = 0.5

# Mensagem inicial do jogo
print(" ====================================\n"
    '|                                     |\n'
    '| Bem-vindo ao INSPER - Batalha Naval |\n'
    '|                                     |\n'
    ' =======   xxxxxxxxxxxxxxxxx   ======= \n')

print('\nIniciando o Jogo!\n') 
time.sleep(t)     # espera 

# Sorteando pais do Computador 
paisSorteado = random.choice(list(PAISES))

# Print do pais do Computador 
print("Computador está alocando os navios de guerra do país {0}...".format(paisSorteado))
print("Computador já está em posição de batalha")
time.sleep(t)     # espera 

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

# Transforma Dicionario de PAISES em lista 
lista_paises = list(PAISES)
pais_jogador = lista_paises[num_pais_jogador-1]

# Informa pais escolhido e instrui jogador a alocar seus navios 
print("Você escolheu a nação {0}".format(pais_jogador))
print("Agora é a sua vez de alocar os seus navios de guerra!")


# fazendo lista de blocos 
lista_blocos_PC = []
for navio,blocos in PAISES[paisSorteado].items():
    lista_blocos_PC.append(blocos)



print(aloca_navios(Mapa_PC,blocos))
print("\n")


#EX de mostrar mapa
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
 
