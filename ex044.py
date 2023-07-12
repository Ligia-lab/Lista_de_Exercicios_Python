# Elabore um programa que calcule o valor a ser pago por um produto, considerando seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:
# À vista dinheiro: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' HELL STORE '))
preço = float(input('Qual o preço do produto? R$ '))
pagamento = int(input('''Qual a forma de pagamento?
[ 1 ]-Dinheiro
[ 2 ]-Débito
[ 3 ]-2x no crédito
[ 4 ]-3x ou mais no crédito
: '''))
if pagamento == 1:
    print('Você terá desconto de 10%, o valor será R$ {:.2f}.'.format(preço - (preço * 0.1)))
elif pagamento == 2:
    print('Você terá desconto de 5%, o valor será R$ {:.2f}.'.format(preço - (preço * 0.05)))
elif pagamento == 3:
    print('Você não terá desconto, serão 2x de R$ {:.2f} sem juros, totalizando R$ {:.2f}.'.format(preço / 2, preço))
elif pagamento == 4:
    parc = int(input('Em quantas vezes será parcelado? '))
    print('Você terá juros de 20%, serão {}x de R$ {:.2f}, totalizando R$ {:.2f}.'.format(parc, (preço + (preço * 0.2))/ parc, preço + (preço * 0.2)))
else:
    print('\033[31mOpção inválida, tente novamente.')