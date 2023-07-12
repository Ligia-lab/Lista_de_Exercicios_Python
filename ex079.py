#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número ja exista la dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados em ordem crescente.

listanum = []
continuar = ''

while True:
    n = int(input('Digite um número: '))
    if n in listanum:
        print('Valor duplicado')
    else:
        listanum.append(n)
        print('Valor adicionado...')

    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'Nn':
        break

print(f'Lista: {sorted(listanum)}')
print('FIM')