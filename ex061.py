#Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão desejada: '))
termo = primeiro
cont = 1

while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo = termo + razao
    cont += 1
print('FIM')