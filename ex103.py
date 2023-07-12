# Faça um programa que tenha uma função chamada ficha(), que receba dois parametros opcionais:
# o nome de um jogador e quantos gols ele marcou.
# O programa devera ser capaz de mostrar a ficha do jogador, mesmo que algum dado nao tenha sido informado corretamente.

def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gols} gol(s) no campeonato.')


# programa principal
nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)