#Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços, na sequencia.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

nome_preco = ('caderno', 15, 'caneta', 3, 'impressora', 650, 'sulfite', 25,
              'caderno', 15, 'caneta', 3, 'impressora', 650, 'sulfite', 25)

print('_' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('_' * 40)

for posicao in range(0, len(nome_preco)):
    if posicao % 2 == 0:
        print(f'{nome_preco[posicao]:.<30}', end='')
    else:
        print(f'R${nome_preco[posicao]:>7.2f}')
print('_' * 40)

'''nome_preco = ('caderno', 15, 'caneta', 3, 'impressora', 650, 'sulfite', 25)

print(f'1- {nome_preco[0]}............R${nome_preco[1]:.2f}')
print(f'2- {nome_preco[2]}.............R${nome_preco[3]:.2f}')
print(f'3- {nome_preco[4]}.........R${nome_preco[5]:.2f}')
print(f'4- {nome_preco[6]}............R${nome_preco[7]:.2f}')'''


