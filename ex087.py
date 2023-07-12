#Aprimore o desafio anterior, mostrando no final:
# A) a soma de todos os valores pares digitados
# B) a soma dos valores da terceira coluna
# C) o maior valor da segunda linha

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = coluna3 = maior2 = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um numero para [{linha}, {coluna}]: '))

print('-=' * 20)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            par += matriz[linha][coluna]
    print()

print('-=' * 20)
print(f'A soma dos pares é {par}')

for linha in range(0, 3):
    coluna3 += matriz[linha][2]
# nesse caso a coluna é fixa, o que varia é a linha
print(f'A soma dos itens da 3ª coluna é {coluna3}')

for coluna in range(0, 3):
    if coluna == 0:
        maior2 = matriz[1][coluna]
    elif matriz[1][coluna] > maior2:
        maior2 = matriz[1][coluna]
# nesse caso a linha é fixa, então tem que percorrer os valores das colunas
print(f'O maior valor da 2ª linha é {maior2}')

#esse codigo ficou maior que o outro pq o outro é manual, mudando o range desse da pra fazer matriz de tamanhos diferentes




'''linha = []
pares = 0
coluna3 = 0
maior = 0

for c in range(0, 9):
    num = int(input('Digite um número: '))
    linha.append(num)
    if num % 2 == 0:
        pares += num
coluna3 = linha[2] + linha[5] + linha[8]

if linha[3] > linha[4] > linha[5]:
    maior = linha[3]
else:
    if linha[4] > linha[5]:
        maior = linha[4]
    else:
        maior = linha[5]

print(f'A soma dos pares é: {pares}')
print(f'A soma da 3ª coluna é: {coluna3}')
print(f'O maior valor da segunda linha é: {maior}')

print(f'[{linha[0]}] [{linha[1]}] [{linha[2]}]')
print(f'[{linha[3]}] [{linha[4]}] [{linha[5]}]')
print(f'[{linha[6]}] [{linha[7]}] [{linha[8]}]')'''
