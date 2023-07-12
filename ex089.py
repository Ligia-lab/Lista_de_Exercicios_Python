#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo numa lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

from time import sleep
boletim = []
aluno = []
c = 0

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    aluno.extend([nome, nota1, nota2, media])
    boletim.append(aluno[:])

    continuar = str(input('Inserir mais notas? [S/N] ')).strip()[0]
    if continuar in 'Nn':
        break
    aluno.clear()

print('-=' * 15)
print(f"{'BOLETIM' : ^30}")
print('-=' * 15)
print(f'{"ID":<5}{"NOME":<10}{"MÉDIA":>12}')
for c in range(0, len(boletim)):
    print(f'{c:<5}{boletim[c][0]:<10}{boletim[c][3]:>12}')
#for indice, aluno in enumerate(boletim):
#    print(f'{indice:<5}{aluno[0]:<10}{aluno[3]:>12}')

while True:
    print('-=' * 15)
    notas = int(input('Mostrar as notas do ID: (999 PARA SAIR) '))
#    print(f'Aluno: {boletim[notas][0:3]}')
    if notas == 999:
        break
    if notas <= len(boletim):
        print(f'Nome: {boletim[notas][0]}      Notas: {boletim[notas][1:3]}')
    else:
        print('ID inválido.')
    sleep(1)
print('FINALIZANDO...')