# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No finaç, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

listanum = []

for c in range(0, 5):
    listanum.append(int(input(f'Digite um número para posição {c}: ')))
print(f'A lista é {listanum}')

print(f'O maior valor foi {max(listanum)} nas posições: ', end='')
for i, v in enumerate(listanum):
    if v == max(listanum):
        print(f'{i}..', end='')
print()
print(f'O menor valor foi {min(listanum)} nas posições: ', end='')
for i, v in enumerate(listanum):
    if v == min(listanum):
        print(f'{i}..', end='')
print()




'''listanum = []
maior = 0
menor = 0

for c in range(0, 5):
    listanum.append(int(input(f'Digite um número para posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]

print(listanum)

print(f'O maior valor foi {maior} nas posições: ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}..', end='')
print()
print(f'O menor valor foi {menor} nas posições: ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}..', end='')
print()'''
