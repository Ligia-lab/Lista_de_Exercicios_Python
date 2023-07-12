# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Insira uma frase: '))
frasesemespaco = frase.replace(' ', '')
fraseminusculo = frasesemespaco.lower()
fraseavesso = fraseminusculo[::-1]
#começa no inicio : termina no fim : lê ao contrário

if fraseminusculo == fraseavesso:
    print('A frase \033[34m{}\033[m é um palindromo!'.format(frase))
else:
    print('Não é um palindromo, ao contrário fica \033[31m{}\033[m.'.format(fraseavesso))




'''frase = str(input('digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de \033[36m{}\033[m é \033[31m{}\033[m.'.format(junto, inverso))
if inverso == junto:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')'''
#solução do professor usando o for
