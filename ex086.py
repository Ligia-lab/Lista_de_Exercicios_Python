#Crie um programa que crie uma matriz de dimensão 3 x 3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um numero para [{linha}, {coluna}]: '))

print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()


'''linha = []


for c in range(0, 9):
    num = int(input('Digite um número: '))
    linha.append(num)

print(f'[{linha[0]}] [{linha[1]}] [{linha[2]}]')
print(f'[{linha[3]}] [{linha[4]}] [{linha[5]}]')
print(f'[{linha[6]}] [{linha[7]}] [{linha[8]}]')'''