# Crie um modulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro(), metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

preço = float(input('Digite o preço: R$'))
print(f'O dobro de R${preço} é R${moeda.dobro(preço)}')
print(f'A metade de R${preço} é R${moeda.metade(preço)}')
print(f'Com aumento de 20% fica R${moeda.aumentar(preço, 20)}')
print(f'Com desconto de 20% fica R${moeda.diminuir(preço, 20)}')

