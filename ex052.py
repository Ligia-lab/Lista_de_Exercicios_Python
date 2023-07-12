#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Insira um número inteiro '))
mult = 0

for count in range (1, n + 1):
    if n % count == 0:
        print('Múltiplo de {}.'.format(count), end= ' ')
        mult += 1
if mult == 2:
    print('\n{} \033[31mÉ\033[m um número primo.'.format(n))
else:
    print('\n{} \033[31mNÃO É\033[m um número primo.'.format(n))
