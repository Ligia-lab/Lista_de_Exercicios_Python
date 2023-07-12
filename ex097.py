#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parametro e mostre uma mensagem com tamanho adaptável.
# ex: escreva('Ola, mundo')
# saida: ~~~~~~~~~~
# saida: Ola, mundo
# saida: ~~~~~~~~~~

def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)


escreva(str(input('Digite um texto: ')))
