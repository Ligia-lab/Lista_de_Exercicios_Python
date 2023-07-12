#Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

cont = 0
soma = 0
maior = 0
menor = 0
continuar = ''

while continuar in 'Ss':
    num = int(input('Insira um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]

media = soma / cont
print('O total de números digitados foi {} e a media deles é {:.2f}.'.format(cont, media))
print('O maior número digitado foi {} e o menor {}.'.format(maior, menor))