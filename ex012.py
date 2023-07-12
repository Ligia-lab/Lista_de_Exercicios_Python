#quanto é o preço com 5% de desconto?

p = float(input('Qual o preço do produto? R$ '))
d = p - p / 100 * 5
print('O preço com desconto é R${:.2f}'.format(d))
