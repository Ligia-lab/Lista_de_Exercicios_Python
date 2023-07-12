#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(l, c):
    a = l * c
    print(f'A área de {l} x {c} é igual a {a}m².')


area(int(input('Digite a largura: ')),
     int(input('Digite o comprimento: ')))