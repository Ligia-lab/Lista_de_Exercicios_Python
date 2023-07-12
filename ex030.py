#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

num = int(input('Escolha um número inteiro: '))
if (num % 2) == 0:
    print('O número {} é PAR.'.format(num))
else:
    print('O número {} é ÍMPAR.'.format(num))