#Desenvolva um programa que leia 6 números inteirose mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

n = 0
soma = 0
cont = 0

for c in range(1, 7):
    n = int(input('Insira o {}º número: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('A soma dos {} números pares é {}'.format(cont, soma))