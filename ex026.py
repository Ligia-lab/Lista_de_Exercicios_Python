# Faça um programa que leia uma frase pelo teclado e mostre :
# Quantas vezes aparece a letra 'A'.
# Em que posição a letra 'A' aparece pela primeira vez.
# Em que posição aparece pela última vez.

frase = str(input('Escreva uma frase: ')).strip().lower()
print('Quantos A tem na frase?', frase.count('a'))
print('Posição do primeiro A:', frase.find('a')+1)
print('Posição do último A:', frase.rfind('a')+1)