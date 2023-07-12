#Faça um programa que leia um número qualquer e mostre seu fatorial.
# ex: 5!=5x4x3x2x1=120

'''from math import factorial

num = int(input('Insira um número pra fazer seu fatorial: '))
fac = factorial(num)

print('O fatorial de {} é {}'.format(num, fac))'''



num = int(input('Fatorial de: '))
count = num
fact = 1

print('Calculando {}!...'.format(num))
while count > 0:
    print('{}'.format(count), end='')
    print(' X ' if count > 1 else ' = ', end='')
    fact = fact * count
    count -= 1
print('{}.'.format(fact))
