# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    num = int(input('TABUADA DO '))
    print('-=' * 20)
    if num < 0:
        break
    for cont in range(1, 11):
        print(f'{num} X {cont} = {num * cont}')
    print('-=' * 20)
print('FIM')
