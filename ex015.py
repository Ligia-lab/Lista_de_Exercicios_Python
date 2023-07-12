#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.


dias = int(input('Por quantos dias ele foi alugado? '))
km = float(input('Quantos Km foram percorridos? '))
ptotal = ( km * 0.15 )+(dias * 60.00)

print('\nO aluguel do carro é de R$60.00 por dia mais R$0.15 por Km rodado.\n')
print('Foram percorridos {}Km em {} dias.\n'.format(km, dias))

print('O valor total do aluguel é R${:.2f}.'.format(ptotal))