#Faça um programa que leia o peso de 5 pessoas. No final mostre qual foi o maior e o menor peso lido.

maior = 0
menor = 0
peso = 0

for p in range(1, 6):
    peso = float(input('{} - insira seu peso: '.format(p)))
    if p == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi {}KG.'.format(maior))
print('E o menor peso foi {}KG.'.format(menor))
