#Faça um programa que calcule a soma entre todos os números ímpares que são multiplos de 3
# e que se encontram no intervalo entre 1 e 500.

soma = 0
cont = 0
for c in range (0, 500, 3):
    if c % 2 == 1:
        cont = cont + 1
        soma += c
print(' os {} numeros somados resultam no valor {}.'.format(cont, soma))

'''soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma dos {} valores é {}.'.format(cont, soma))'''
