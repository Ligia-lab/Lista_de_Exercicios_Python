#Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A) qual o total gasto na compra
# B) quantos produtos custam mais de R$1000
# C) qual o nome do produto mais barato.

nome = ' '
preco = 0
total = 0
mais_mil = 0
mais_barato = 0
nome_barato = ' '
cont = 1

while True:
    print('-=' * 20)
    print(f'PRODUTO {cont}')

    nome = str(input('Qual no nome do produto? ')).upper().strip()
    preco = float(input('Qual o valor do produto? R$'))
    total += preco
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if cont == 1:
        mais_barato = preco
        nome_barato = nome
    else:
        if preco < mais_barato:
            mais_barato = preco
            nome_barato = nome
    if preco > 1000:
        mais_mil += 1
    if continuar == 'N':
        print('FINALIZANDO...')
        break
    cont += 1

print(f'\nO total gasto foi de R${total:.2f}.')
print(f'Apenas {mais_mil} produtos custaram mais de R$1000,00')
print(f'O produto mais barato foi {nome_barato}, por R${mais_barato:.2f}')
print('FIM')





'''nome = ''
preco = 0
total = 0
mais_mil = 0
cont = 1

while True:
    print(f'PRODUTO {cont}')
    print('-=' * 20)
    nome = str(input('Qual no nome do produto? ')).upper().strip()
    preco = float(input('Qual o valor do produto? R$'))
    cont += 1
    total += preco
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if preco > 1000:
        mais_mil += 1
    if continuar == 'N':
        print('FINALIZANDO...')
        break

print(f'O total gasto foi de R${total:.2f}.')
print(f'{mais_mil} produtos custaram mais de R$1000,00')
print('FIM')

'''