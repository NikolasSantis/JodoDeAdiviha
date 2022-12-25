from time import sleep
from os import system
def Player1():
    system("clear")
    print('--'*20)
    print(f'{"JOGO DE ADIVINHAÇÃO".center(40)}')
    print('--'*20)
    while True:
        try:
            numJogador1 = int(input('Número escolhido pelo Jogador 1 (0 a 10): '))
        except (ValueError, TypeError):
            print('Digite apenas números inteiros.')
        else:
            if numJogador1 > 10 or numJogador1 < 0:
                print('Erro! Valores de 0 a 10 apenas')
            else:
                break
    Player2(numJogador1)
    
def Player2(numJogador1):
    system("clear")
    print('--'*20)
    print(f'{"JOGO DE ADIVINHAÇÃO".center(40)}')
    print('--'*20)
    print('O Jogador 1 escolheu um número de 0 a 10')
    print('--'*20)
    tentativas = 0
    numerosJogador2 = []
    while True:
        while True:
            try:
                numJogador2 = int(input('Que número é esse? '))
            except (ValueError, TypeError):
                print('Erro. Digite numeros inteiros')
            else:
                if numJogador2 > 10 or numJogador2 < 0:
                    print('Digite numeros de 0 a 10 apenas.')
                else:
                    break
        numerosJogador2.append(numJogador2)
        tentativas += 1
        if numJogador2 == numJogador1:
            break
        else:
            print('Não é esse o número, tente outra vez')
    print('--'*20)
    print(f'{f"PARABÉNS O NÚMERO ERA {numJogador2}".center(40)}')
    print('--'*20)
    print(f'Total de números palpitados {len(numerosJogador2)} ')
    print('Os números palpitados foram:')
    c = 0 
    while c < len(numerosJogador2):
        print(f'{numerosJogador2[c]} ', end='')
        c += 1
    print(f'\nO número de tentativas foi: {tentativas}')
                
        