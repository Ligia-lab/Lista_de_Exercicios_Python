#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre
# A)quantas pessoas foram cadastradas
# B) uma listagem com as pessoas mais pesadas
# C) uma listagem com as pessoas mais leves

temporaria = []
principal = []
maior = menor = 0

while True:
    temporaria.append(str(input('Nome: ')))
    temporaria.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    resposta = str(input('Quer continuar? [S/N] ')).strip()[0]
    if resposta in 'Nn':
        break

print('-=' * 30)
print(f'Os dados cadastrados foram: {principal}')
print(f'Ao todo você cadastrou {len(principal)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de: ', end='')
for pessoa in principal:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de : ', end='')
for pessoa in principal:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}] ', end='')
print()


'''pessoas = []
lista = []
pesadas = []
leves = []

while True:
    nome = str(input('Digite seu nome: '))
    peso = float(input('Digite seu peso: '))
    pessoas.append(nome)
    pessoas.append(peso)
    continuar = str(input('Quer continuar? [S/N] ')).strip()[0]
    lista.append(pessoas[:])
    if peso > 80:
        pesadas.append(nome)
        pesadas.append(peso)
    elif peso < 60:
        leves.append(nome)
        leves.append(peso)
    pessoas.clear()
    if continuar in 'Nn':
        break
print('-=' * 30)
print(f'{len(lista)} pessoas foram cadastradas')
print(f'As pessoas mais pesadas foram: {pesadas}')
print(f'As pessoas mais leves foram: {leves}')'''