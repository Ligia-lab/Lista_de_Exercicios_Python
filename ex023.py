#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos
# digitos separados ( unidade, centena, dezena e milhar)

numero = int(input('Digite um numero de 0 a 9999 diígitos: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('No número {} temos'.format(numero))
print('Unidade:{}'.format(u))
print('Dezena: {}'.format(d))
print('Centena:{}'.format(c))
print('Milhar: {}'.format(m))