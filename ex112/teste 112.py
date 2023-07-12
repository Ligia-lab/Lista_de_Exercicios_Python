# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
# mas com uma validação de dados para aceitar apenas valores que sejam monetários.

from ex112.UtilidadesCeV112 import dados
from ex112.UtilidadesCeV112 import moeda


preço = dados.leia_dinheiro('Digite o preço: R$')
moeda.resumo(preço, 20, 15)

