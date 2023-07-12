#Crie um programa que gerencie o aproveitamento de um jogadorr de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
jogador['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
totgol = 0
c = 0
gols = []

while c < partidas:
    gols.append(int(input(f'Na partida {c+1} fez: ')))
    c += 1

jogador['Gols'] = gols[:]
jogador['Total de gols'] = sum(gols)

print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f' O campo {k} tem valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} fez {len(jogador["Gols"])} partidas.')
for i, v in enumerate(jogador['Gols']):
    print(f'     Na partida {i+1} foram feitos {v} gols.')
print(f'Foi um total de {jogador["Total de gols"]}.')
