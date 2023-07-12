# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108, 109 e 110 para o primeiro pacote e mantenha tudo funcionando.

from ex112.UtilidadesCeV import moeda
from ex111.UtilidadesCeV import dados


preço = float(input('Digite o preço: R$'))
moeda.resumo(preço, 20, 15)

