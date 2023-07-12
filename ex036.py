# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o VALOR da casa, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário mensal? R$ '))
tempo = int(input('Quantos anos de financiamento? '))
tempomes = (tempo * 12)
valormes = valor / tempomes
if valormes > (salario * 0.3):
    print('EMPRÉSTIMO NEGADO! \nA prestação mensal seria de R$ {:.2f}, que excede 30% do seu salário.'.format(valormes))
else:
    print('APROVADO! \nA prestação mensal será de R$ {:.2f}, que serão pagos em {} meses.'.format(valormes, tempomes))

