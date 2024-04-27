from dados import * 
import random 
import time 


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

# Printar dicionario de paises e seus navios com delay de 1 segundo
i = 1 
for pais,infos in PAISES.items(): 
    print(str(i)+":",pais)
    for navio,blocos in infos.items():
        print("  ",blocos,navio)
    print("")
    i+=1