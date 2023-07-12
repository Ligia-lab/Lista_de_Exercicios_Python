# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso , mostre a listagem de numeros gerados e tambem indique o menor e o maior que estao na tupla.

from random import randint

num = (randint(0, 10), randint(0, 10), randint(0, 10),
       randint(0, 10), randint(0, 10), )

print('Os valores sorteados foram: ', end='')
for n in num:
    print(f' {n}', end='')
print(f'\nO maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')


'''num = (randint(0, 10), randint(0, 10), randint(0, 10),
       randint(0, 10), randint(0, 10), )
maior = 0
menor = 0

print('SORTEADNDO...')

for cont in range(0, len(num)):
    print(num[cont], end=' ')
    if cont == 0:
        maior = num[cont]
        menor = num[cont]
    else:
        if num[cont] > maior:
            maior = num[cont]
        if num[cont] < menor:
            menor = num[cont]

print(f'\nO maior foi {maior}.')
print(f'O menor foi {menor}.')'''
