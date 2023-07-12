#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai coloca-los dentro da lista e a
# segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores para a lista....')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('\nFIM')


def soma_par(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares da lista {lista}, temos {soma}.')


numeros = []
sorteia(numeros)
soma_par(numeros)

'''num = []


def sorteia():
    for c in range(0, 5):
        num.append(randint(0, 10))


def somaPar():
    par = 0
    for c in range(0, len(num)):
        if num[c] % 2 == 0:
            par += num[c]
        c += 1
    print(par)


sorteia()
print(num)
print(f'A soma dos pares é ', end='')
somaPar()'''
