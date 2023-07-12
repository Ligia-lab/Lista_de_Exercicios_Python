# O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

n1 = input('Nome 1: ')
n2 = input('Nome 2: ')
n3 = input('Nome 3: ')
n4 = input('Nome 4: ')
nomes = [n1, n2, n3, n4]
random.shuffle(nomes)

print('A ordem de apresentação é: {}'.format(nomes))
