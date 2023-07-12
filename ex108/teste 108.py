# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.

import moeda

preço = float(input('Digite o preço: R$'))
print(f'O dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}')
print(f'A metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}')
print(f'Com aumento de 20% fica {moeda.moeda(moeda.aumentar(preço, 20))}')
print(f'Com desconto de 20% fica {moeda.moeda(moeda.diminuir(preço, 20))}')

