# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvido no desafio 108.

import moeda

preço = float(input('Digite o preço: R$'))
print(f'O dobro de {moeda.moeda(preço)} é {moeda.dobro(preço, True)}')
print(f'A metade de {moeda.moeda(preço)} é {moeda.metade(preço, True)}')
print(f'Com aumento de 20% fica {moeda.aumentar(preço, 20, True)}')
print(f'Com desconto de 20% fica {moeda.diminuir(preço, 20, True)}')

