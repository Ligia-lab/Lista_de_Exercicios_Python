#Crie um programa que leia o ano de nascimento de 7 pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas são maiores.

from datetime import date

maior = 0
menor = 0

for pessoa in range(1, 8):
    ano = int(input('{} - Informe o seu ano de nascimento: '.format(pessoa)))
    idade = date.today().year - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('{} pessoas são maiores.'.format(maior))
print('{} pessoas ainda são menores.'.format(menor))
