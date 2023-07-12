#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7,00 para cada km acima do limite.

vel = float(input('Qual a velocidade do carro? '))
mul = (vel - 80) * 7
if vel > 80:
    print('ACIMA DA VELOCIDADE PERMITIDA')
    print('Sua multa será de R${:.2f}.'.format(mul))
else:
    print('Tenha um bom dia.')
