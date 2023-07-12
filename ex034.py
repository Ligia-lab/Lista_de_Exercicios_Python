#Escreva um programa que pergunte o ssalário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais a R$1250,00 o aumento é de 15%.

sal = float(input('Qual o valor do seu salário? R$'))
if sal <= 1250.00:
    print('O seu aumento será de 15% (R${:.2f}), totalizando R${:.2f}.'.format(sal*0.15, sal*0.15+sal))
else:
    print('O seu amuneto será de 10% (R${:.2f}), totalizando R${:.2f}.'.format(sal*0.10, sal*0.10+sal))

#o professor colocou o calculo em novas variáveis e colocou só um print