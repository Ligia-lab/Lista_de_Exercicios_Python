#Faça um programa que ajude um jogador da mega sena a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cdastrando tudo em uma lista composta.

import time
from random import randint

print('-=' * 30)
print(f"{'MEGA-SENA': ^60}")
print('-=' * 30)

jogos = []
palpite = []
quantidade = int(input('Quantos jogos você quer gerar: '))
num = 0

print('-=' * 30)
for c in range(0, quantidade):
    while len(palpite) < 6:   #ele fez com contador, se contador >= 6 ----break ---- contador += 1
        num = randint(1, 60)
        if num not in palpite:
            palpite.append(num)

    jogos.append(palpite[:])
    palpite.clear()
    print(f'{c + 1}- {sorted(jogos[c])}')
    time.sleep(0.5)

# for i, l in enumerate(jogos): fora da identação para imprimir linha por linha

print('-=' * 30)
print(f"{'BOA SORTE': ^60}")