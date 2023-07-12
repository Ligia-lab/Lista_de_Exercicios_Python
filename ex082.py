#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados , respectivamente.
# No final, mostre o conteúdo das três listas geradas.

lista = []
lista_par = []
lista_impar = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'Nn':
        break

'''for i, v in enumerate(lista):
    if v % 2 == 0:
        lista_par.append(v)
    else:
        lista_impar.append(v)'''

for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        lista_par.append(lista[c])
    elif lista[c] % 2 == 1:
        lista_impar.append(lista[c])


print('FIM')
print(f'Lista Mãe: {lista}')
print(f'ÍMPARES: {lista_impar}')
print(f'PARES: {lista_par}')
