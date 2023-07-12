#Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) quantas vezes apareceu o valor 9
# B) em que posiçaõ foi digitado o primeiro valor 3
# C) quais foram os numeros pares.

valores = (int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')))
print(f'Você digitou os números {valores}.')
print(f'O valor 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O número 3 apareceu pela primeira vez na {valores.index(3) + 1}ª posição.')
print('O valores pares digitados foram: ', end=' ')

for n in valores:
    if n % 2 == 0:
        print(n, end=' ')


'''valores = (int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')))
print(f'Você digitou os números {valores}.')
cont = 0
cont9 = 0
par = 0
nome_par = ''

for cont in range(0, len(valores)):
    if valores[cont] == 9:
        cont9 += 1
    if valores[cont] % 2 == 0:
        par += 1
        nome_par = valores[cont]
        print(f'{nome_par} ', end='')
print('são pares.')
if 3 in valores:
    print(f'O numero 3 apareceu na {valores.index(3) + 1}ª posição.')
print(f'O numero 9 foi digitado {cont9} vezes.')'''

