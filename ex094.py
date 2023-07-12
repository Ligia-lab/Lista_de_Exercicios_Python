# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionário em uma lista. No final, mostre:
# A) quantas pessoas foram cadastrada
# B) A média de idade do grupo
# C) Uma lista com todas as mulheres
# D) uma Lista com todas as pessoas com idade acima da média

galera = []
pessoa = {}
soma = media = 0

#leitura dos dados
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite o nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite [M/F].')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        resposta = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Digite [S/N].')
    if resposta == 'N':
        break

#análise dos dados
print('-=' * 30)
print(f'A) Foram cadastradas {len(galera)} pessoas.')

media = soma / len(galera)
print(f'B) A média de idade do grupo é de {media:.0f} anos.')

print('C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()

print('D) Pessoas com idade acima da média: ')
for p in galera:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'    {k} = {v}', end='')
        print()
print(' >>> ENCERRADO <<<')

help(print)