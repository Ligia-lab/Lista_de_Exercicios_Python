# Aprimore o desafio 93 para que ele funcione com varios jogadores, incluindo um sistema de vizualização de detalhes de aproveitamento de cada jogador.

time = []
jogador = {}
partidas = []

#entrada de dados
while True:
    jogador.clear()
    partidas.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))

    for c in range(0, tot):
        partidas.append(int(input(f'Na partida {c+1} fez: ')))
    jogador['Gols'] = partidas[:]
    jogador['Total de gols'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda S/N.')
    if resp == 'N':
        break

# mostra de dados
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15} ', end='')
print()
print('--' * 30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15} ', end='')
    print()
print('--' * 30)
while True:
    busca = int(input('Quer ver os dados de qual jogador (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO!, Não existe jogador com código {busca}.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}: ')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('--' * 30)
print('-=' * 30)
print('>>> VOLTE SEMPRE <<<')
