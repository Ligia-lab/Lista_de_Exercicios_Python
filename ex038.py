# Escreva um programa que leia 2 números inteiros e compare-os, mostrando na tela uma mensagem:
# - o primeiro valor é maior
# - o segundo valor é maior
# - não existe valor maior, os dois são iguais

n1 = int(input('Insira um número inteiro: '))
n2 = int(input('Insira outro número inteiro: '))
if n1 > n2:
    print('O primeiro valor ({}) é maior.'.format(n1))
elif n2 > n1:
    print('O segundo valor ({}) é maior.'.format(n2))
else:
    print('Não existe valor maior, eles são iguais.')
