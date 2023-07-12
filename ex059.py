#Crie um programa que leia dois valores e mostre um menu na tela:
# [1]somar
# [2]multiplicar
# [3]maior
# [4]novos números
# [5]sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

a = int(input('Insira um número: '))
b = int(input('Insira outro número: '))
menu = 0

while menu != 5:
    print('MENU: ')
    print('''    [1]somar
    [2]multiplicar
    [3]maior
    [4]novos números
    [5]sair''')
    menu = int(input('>>>>Opção: '))

    if menu == 1:
        print('A soma é {}'.format(a + b))
    elif menu == 2:
        print('A multiplicação é {}'.format(a * b))
    elif menu == 3:
        if a > b:
            print('{} é maior que {}'.format(a, b))
        elif b > a:
            print('{} é maior que {}'.format(b, a))
        else:
            print('Os dois números são iguais')
    elif menu == 4:
        a = int(input('Insira um número: '))
        b = int(input('Insira outro número: '))
    elif menu == 5:
        print('Finalizando...')
    elif menu > 6:
        print('Opção inválida')
    print('=-=' * 10)
    sleep(1)

print('FIM')