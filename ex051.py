# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos  dessa progressão.

print('==' * 21)
print('*{:^40}*'.format(' 10 TERMOS DE UMA PA '))
print('==' * 21)

primeiro = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a razão: '))
n = int(input('Quantos elementos: '))
# o n se refere a quantidade de elementos, na aula ele ja usou o n fixo em 10
ultimo = primeiro + (n - 1) * razao

for c in range (primeiro, ultimo + razao, razao):
     print('{}'.format(c), end= ' > ')
print('FIM')
