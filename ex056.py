#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
mulher_menos_20 = 0

for count in range(1, 5):
    print('----{}ª PESSOA----'.format(count))
    nome = input('NOME: ').strip()
    idade = int(input('IDADE: '))
    sexo = input('SEXO [F/M]: ').strip()
    soma_idade += idade

    if sexo in 'Mm' and count == 1:
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulher_menos_20 += 1

media_idade = soma_idade / 4
print('A média de idade é {} anos.'.format(media_idade))
print('O homem mais velho é o {} e tem {} anos.'.format(nome_mais_velho, maior_idade_homem))
print('Temos {} mulheres menores de 20 anos.'.format(mulher_menos_20))