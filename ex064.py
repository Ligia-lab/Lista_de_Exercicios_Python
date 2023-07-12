#Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o unuário digitar o valo 999 que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

'''num = 0
count = 0
soma = 0

while num != 999:
    num = int(input('Insira um número [999 para finalizar]: '))
    count += 1
    if num != 999:
        soma += num
print('O total de números digitados foi {} e a soma deles é {}.'.format((count - 1), soma))''' # meu codigo

cont = soma = 0

num = int(input('Insira um número [999 para finalizar]: '))
while num != 999:
        cont += 1
        soma += num
        num = int(input('Insira um número [999 para finalizar]: '))
print('O total de números digitados foi {} e a soma deles é {}.'.format(cont, soma))
