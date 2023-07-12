#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário.
# No finsl, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
ranking = []

print('Valores sorteados')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # ******************************* Os valores do dicionário são jogados na LISTA ranking
print('-=' * 20)
print('          == RANKING ==')
for i, v in enumerate(ranking):    #por ser uma LISTA  usa enumerate/// i = indice    v = valor //// enumerate percorre os elementos da lista
    print(f'    {i + 1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
