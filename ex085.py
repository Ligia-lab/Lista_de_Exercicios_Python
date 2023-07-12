#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e impares.
# No final, mostre os valores pares e impares em ordem crescente.

num = [[], []]
valor = 0

for c in range(0, 7):
    valor = int(input(f'Digite o {c + 1}º número: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print('-=' * 30)
print(f'PARES: {sorted(num[0])}')
print(f'ÍMPARES: {sorted(num[1])}')
print(f'A lista completa: {num}')