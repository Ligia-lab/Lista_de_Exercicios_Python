#Crie um programa que simule o funcionamento de um caixa eletronico.
# No inicio, pergunte ao usuário o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui notas de R$50, R$20, R$10 e R$1.

valor = int(input('Qual valor quer sacar? R$'))
total = valor
cedula = 50
total_cedula = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break
print('Finalizando...')



'''saque = int(input('QUAL O VALOR DO SAQUE: R$'))

nota50 = saque // 50
valor50 = nota50 * 50

nota20 = (saque - valor50) // 20
valor20 = nota20 * 20

nota10 = (saque - valor50 - valor20) // 10
valor10 = nota10 * 10

nota1 = saque - valor10 - valor50 - valor20

print(f'\nPara sacar R${saque} precisamos de:')
if nota50 != 0:
    print(f'\n{nota50} notas de R$50,00')
if nota20 != 0:
    print(f'{nota20} notas de R$20,00')
if nota10 != 0:
    print(f'{nota10} notas de R$10,00')
if nota1 != 0:
    print(f'{nota1} notas de R$1,00')'''