#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é maior.

from time import sleep


def maior(* num):
    cont = maior = 0
    print('-=' * 25)
    print('Analisando valores....')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print()
    print(f'Foram informados {cont} valores e o maior é {maior}.')


maior(1, 5, 9, 4, 2)
maior(8, 3, 2, 100, 12, 5, 3)
maior(1, 2, 3)

