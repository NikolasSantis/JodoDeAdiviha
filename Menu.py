from VersusCPU.WithCPU import *
from VersusPlayer.Multiplayer import *
from time import sleep
from os import system
system("clear")
print('--'*20)
print(f'{"MODOS DE JOGO".center(40)}')
print('--'*20)
print('1° Jogador VS Jogador ')
print('2° Jogador VS CPU')
print('3° CPU VS Jogador')
print('4° Sair do Jogo')
while True:
    try:
        modoDeJogo = int(input('Modelo escolhido: '))
    except (ValueError, TypeError):
        print('Erro. Digite um valor inteiro')
    else:
        if modoDeJogo != 1 and modoDeJogo != 2 and modoDeJogo !=3 and modoDeJogo!= 4:
            print('Digite apenas "1", "2" ou "3"')
        else:
            break
if modoDeJogo == 1:
    Player1()
elif modoDeJogo == 2:
    CpuVsPlayer()
elif modoDeJogo == 3:
    VsCPU()
print('\n--'*20)
print(f'{"SAINDO DO JOGO...".center(40)}')
print('--'*20)
sleep(1.3)
