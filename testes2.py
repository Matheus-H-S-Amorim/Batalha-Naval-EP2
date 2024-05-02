from funcoes import * 
from dados import *
import time 

jogar_dnv = "s"

while jogar_dnv=="s":
    # Cria mapas para PC e JOGADOR
    Mapa_PC_oculto = cria_mapa(10)
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
    print("Computador já está em posição de batalha!")
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
    while num_pais_jogador not in range(1,5):
        print("Entrada inválida. DIgite outro numero de nação")
        num_pais_jogador= int(input("Qual o número da nação da sua frota?: "))


    # Transforma Dicionario de PAISES em lista 
    lista_paises = list(PAISES)
    pais_jogador = lista_paises[num_pais_jogador-1]

    # Informa pais escolhido e instrui jogador a alocar seus navios 
    print("Você escolheu a nação {0}".format(pais_jogador))
    print("Agora é a sua vez de alocar os seus navios de guerra!")


    # Preencher MAPA_PC  (VEZ UNICA)
    lista_blocos_PC = []                                   # Cria lista de blocos dos navios pro pc 
    for navio,blocos in PAISES[paisSorteado].items():
        lista_blocos_PC.append(blocos)

    aloca_navios(Mapa_PC,lista_blocos_PC)                  # aloca navios(blocos) no Mapa do pc


    #Mostra MAPA_PC_Oculto e MAPA_JOGADOR
    print('COMPUTADOR - {0}'.format(paisSorteado))
    print(mostra_mapa(Mapa_PC_oculto,ALFABETO))

    print('JOGADOR - {0}'.format(pais_jogador))
    print(mostra_mapa(Mapa_Jog,ALFABETO))


    # Preenche MAPA_JOGADOR (fica em looping até acabar navios da frota)
    Preenche_MAPA_JOG(PAISES,Mapa_Jog,Mapa_PC_oculto,ALFABETO,pais_jogador)

    # Falar que jogo vai começar 
    print(mostra_mapa(Mapa_PC_oculto,ALFABETO))
    print(mostra_mapa(Mapa_Jog,ALFABETO))
    print("Iniciando batalha naval")
    time.sleep(t*2)     
    print("5")
    time.sleep(t*2)     
    print("4")
    time.sleep(t*2)     
    print("3")
    time.sleep(t*2)     
    print("2")
    time.sleep(t*2)     
    print("1")

    ########## so vendo oq tem nas matrizes 
    #print('mapajog:',Mapa_Jog)
    #print('mapapc: ,',Mapa_PC)
    #print('mapapcoculto :',Mapa_PC_oculto)


    print("colinha abaixo")
    print(mostra_mapa(Mapa_PC,ALFABETO))


    print("jogador atacando.............")
    JOG_Ataca_PC(PAISES,Mapa_Jog,Mapa_PC_oculto,Mapa_PC,ALFABETO,pais_jogador,paisSorteado)

    print("pc atacando.............")
    PC_Ataca_JOG(PAISES,Mapa_Jog,Mapa_PC_oculto,Mapa_PC,ALFABETO,pais_jogador,paisSorteado)




    while foi_derrotado(Mapa_PC)==False and foi_derrotado(Mapa_Jog)==False: 
        print("Jogador atacando.............")
        JOG_Ataca_PC(PAISES,Mapa_Jog,Mapa_PC_oculto,Mapa_PC,ALFABETO,pais_jogador,paisSorteado)

        print("Pc atacando.............")
        PC_Ataca_JOG(PAISES,Mapa_Jog,Mapa_PC_oculto,Mapa_PC,ALFABETO,pais_jogador,paisSorteado)
    if foi_derrotado(Mapa_PC)==True: 
        print("Você venceu!")
        print("Temos um novo xerife nos mares!")
    elif foi_derrotado(Mapa_Jog)==True: 
        print("Você perdeu!")
        print("Tente novamente outra vez!")

    jogar_dnv = input("JOgar novamente? [s/n]").lower() 
    
    while jogar_dnv not in ["s","n"]: 
        print("Resposta inválida. Digite s ou n!")
        jogar_dnv = input("JOgar novamente? [s/n]").lower() 





