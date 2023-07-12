#Melhore o jogo do desafio 028 onde o computador vai pensar um número de 0 a 10.
# Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

print('==*' * 18)
print('Você consegue advinhar o número que estou pensando????')
print('==*' * 18)

from random import randint
computador = randint(1,10)
jogador = 0
chute = 0

while jogador != computador:
    jogador = int(input('Escolha um número de 0 a 10: '))
    if jogador == computador:
        print('BOOOOA!')
    else:
        if jogador > computador:
            print('Menos... tente de novo')
            chute += 1
        elif jogador < computador:
            print('Mais... tente de novo')
            chute += 1

print('Parabéns! O número soteado foi {} e você chutou {} vezes até acertar.'.format(computador, chute))
