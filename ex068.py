#Faça um programa que jogue par ou impar com o computador.
#O jogo será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

n1 = 0
soma = 0
cont = 0
jogador = ''

while True:
    print('~~' * 20)
    print(f'RODADA {cont + 1}')
    print('~~' * 20)
    jogador = str(input('Par ou Ímpar: ')).upper().strip()[0]

    if jogador not in 'PI':
        print('Inválido, tente novamente.')
    else:
        n1 = int(input('Escolha um número: '))
        n2 = randint(1, 10)
        print(f'O computador escolheu {n2}')
        soma = n1 + n2

        if soma % 2 == 0:
            print(f'O numero {soma} é PAR')
            if jogador == 'P':
                print('GANHOU!!')
            else:
                break
        if soma % 2 == 1:
            print(f'O número {soma} é ÍMPAR.')
            if jogador == 'I':
                print('GANHOU!!')
            else:
                break
        cont += 1

print(f'\nVOCÊ PERDEU! O total de vitórias consecutivas foi {cont}.')
