#Desenvolva um programaque pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens até 200Km e R$0,45 para viagens mais longas.

dis = float(input('Qual a distância em Km a ser percorrida? '))
if dis <= 200:
    print('O valor da passagem será R${:.2f}.'.format(dis * 0.50))
else:
    print('O valor da passagem será R${:.2f}.'.format(dis * 0.45))