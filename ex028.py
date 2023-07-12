#Escreva um programa que faça o computador 'pensar' em um número inteiro de 0 a 5
# e peça pro usuário descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
import time
num = random.randint(0,5)
print('->>' * 20)
print('Você consegue advinhar o número que estou pensando?????')
print('->>' * 20)
num2 = int(input('Escolha um número de 0 a 5: '))
print('PROCESSANDO...')
time.sleep(2)
if num == num2:
    print('Parabéns! Você acertou!')
else:
    print('Que pena, você errou!')
print('O número sorteado foi {}!'.format(num))
