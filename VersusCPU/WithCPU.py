from time import sleep
from os import system
from random import randint
def WithCPU():
    system("clear")
    print('--'*20)
    print(f'{"JOGO DE ADIVINHAÇÃO".center(40)}')
    print('--'*20)
    while True:
        try:
            numJogador = int(input('Digite um número de 0 a 10: '))
        except (TypeError, ValueError):
            print('Tente novamente')
        else:
            if numJogador > 10 or numJogador < 0:
                print('Erro! Valores de 0 a 10 apenas')
            else:
                break
    print('--'*20)
    print(f'{"ATENÇÃO".center(40)}')
    print(f'{"A TELA IRÁ SE APAGAR ".center(40)}')
    print('--'*20)
    contnue = str(input('Digite quando estiver pronto para prosseguir: '))
    print('--'*20)
    system("clear")
    print('--'*20)
    print(f'{"JOGO DE ADIVINHAÇÃO".center(40)}')
    print('--'*20)
    tentativas = 1
    rept = []
    while True:
        comp = randint(0, 10)
        while True:
            if comp in rept:
                comp = randint(0, 10)
            else:
                rept.append(comp)
                break
        while True:
            try:
                result = str(input(f'O número escolhido foi {comp}? [S/N] '))[0].upper().strip()
                if result.isnumeric():
                  resut = int(result)
            except (ValueError, TypeError):
                print('Tente Novamente')
            else:
                break
    
        if result == 'S':
            break
        elif result == 'N':
            print('Buscando outro número...')
            tentativas += 1
            sleep(1.3)
        else:
            print('ERRO! Digite apenas "S" ou "N"')
            rept.pop(tentativas - 1)
    print('--'*20)
    print('Números que o computador jogou: ', end='')
    c = 0
    while c < len(rept):
      print(f'{rept[c]} ', end='')
      c += 1
    print()
    print('--'*20)
    print(f'Números de tentativas do computador: {tentativas}')
    print(f'Número escolhido pelo usuário: {numJogador}')
    print('=='*20)
    print(f'{"ENCERRANDO":>24}', end='')
    for c in range(0, 3):
        print('.', end='')
        sleep(1)
    print()
    print('=='*20)
