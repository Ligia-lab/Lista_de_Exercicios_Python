#Faça um programa que tenha uma função chamada contador(), que receba três parametros: inicio, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# A) de 1 ate 10, de 1 em 1
# B)de 10 até 0, de 2 em 2
# C) uma contagem personalizada.

from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-=' * 25)
    print(f' Contagem de {inicio} até {fim} pulando de {passo} em {passo}.')
    sleep(0.5)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='')
            cont += passo
            sleep(0.3)
        print('FIM')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)  # desnecessario, mas serve pra não bufferizar
            cont -= passo
            sleep(0.3)
        print('FIM')

    '''for c in range(inicio, fim, passo):
        print(f'{c} ', end='')
        sleep(0.3)
    print('FIM')'''  # desse jeito da erro quando a contagem for reversa


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 25)
print('É sua vez!')
contador(int(input('Inicio: ')),
         int(input('Fim: ')),
         int(input('Passos: ')))