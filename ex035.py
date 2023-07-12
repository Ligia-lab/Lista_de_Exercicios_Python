#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Insira o valor da primeira reta: '))
r2 = float(input('Insira o valor da segunda reta: '))
r3 = float(input('Insira o valor da terceira reta: '))
if (r1 + r2 > r3) and (r2 + r3 > r1) and (r3 + r1 > r2):
    print('PODE formar um triângulo!')
else:
    print('NÃO PODE formar um triângulo.')