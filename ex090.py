#Faça um programa que leia nome e média de um aluno, guardando também a situação da nota em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = {}

aluno['NOME'] = str(input('NOME: '))
aluno['MÉDIA'] = float(input(f'MÉDIA DE {aluno["NOME"]}: '))

if aluno['MÉDIA'] >= 7:
    aluno['SITUAÇÃO'] = 'APROVADO'
elif aluno['MÉDIA'] < 5:
    aluno['SITUAÇÃO'] = 'REPROVADO'
else:
    aluno['SITUAÇÃO'] = 'RECUPERAÇÃO'

print('-=' * 15)
for k, v in aluno.items():
    print(f'{k} = {v}')
