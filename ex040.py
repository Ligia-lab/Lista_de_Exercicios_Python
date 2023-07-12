# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média antre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2)/ 2
if m < 5:
    print('REPROVADO\nMédia {:.2f}'.format(m))
elif m >= 5 and m < 7:
    print('RECUPERAÇÃO\nMédia {:.2f}'.format(m))
elif m >= 7:
    print('APROVADO\nMédia {:.2f}'.format(m))