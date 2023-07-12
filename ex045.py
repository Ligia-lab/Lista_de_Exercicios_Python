# Crie um programa que faça o compuatdor jogar jokenpô com você.

'''from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('Suas opções:\n[ 0 ] PEDRA \n[ 1 ] PAPEL\n[ 2 ] TESOURA')
jogador = int(input('qual sua jogada? '))
print('-=' * 15)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 15)
if computador == 0: #pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('JOGADOR PERDE')
elif computador == 1: #papel
    if jogador == 0:
        print('JOGADOR PERDE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
elif computador == 2: #tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('JOGADOR PERDE')
    elif jogador == 2:
        print('EMPATE')'''



import random
print('{:=^50}'.format('\033[34m JOKENPO \033[m'))
player = input('Escolha uma mão: ').upper().strip()
comp = ['PEDRA', 'PAPEL','TESOURA']
compr = random.choice(comp)
print('O computador escolheu \033[37m{}.'.format(compr))
if player == 'PEDRA' and compr == 'TESOURA':
    print('\033[36mGANHOU! {} ganha de {}.'.format(player, compr))
elif player == 'TESOURA' and compr == 'PAPEL':
    print('\033[36mGANHOU! {} ganha de {}.'.format(player, compr))
elif player == 'PAPEL' and compr == 'PEDRA':
    print('\033[36mGANHOU! {} ganha de {}.'.format(player, compr))
elif player == compr:
    print('\033[33mEMPATE')
else:
    print('\033[31mPERDEU! {} ganha de {}.'.format(compr, player))
