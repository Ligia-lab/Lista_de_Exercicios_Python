#Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
num = [n1, n2, n3]
print('O maior número é {}.'.format(max(num)))
print('O menor número é {}.'.format(min(num)))

#o professor fez usando if comparando os trê números