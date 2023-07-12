# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base da conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

num = int(input('Insira um número inteiro qualquer: '))
conv = int(input('''Escolha a base de conversão. 
Use:
[ 1 ] para binário
[ 2 ] para octal
[ 3 ] para hexadecimal
Escolha:'''))
if conv == 1:
    print('{} Convertido em binário é {}.'.format(num, bin(num)[2:]))
elif conv == 2:
    print('{} Convertido em octal é {}.'.format(num, oct(num)[2:]))
elif conv == 3:
    print('{} Convertido em hexadecimal é {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida.')