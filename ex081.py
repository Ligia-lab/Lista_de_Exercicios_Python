#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) quantos números foram digitados
# B) a lista de valores, ordenada de forma decrescente
# C) se o valor 5 foi digitado e está ou não na lista

lista = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'Nn':
        print('Finalizando...')
        break

print('=-' * 30)
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista decrescente é {lista}.')
if 5 in lista:
    print('O valor 5 FAZ parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
