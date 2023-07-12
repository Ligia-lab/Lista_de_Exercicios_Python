#  Crie um programa que tenha uma tupla totalmente preenchida com uma contagem de extenso de 0 até 20.
#  Seu programa deverá ler um número pelo teclado( entre 0 e 20) e mostrá-lo por extenso.

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desesseis', 'desessete', 'dezoito', 'desenove', 'vinte')

while True:
    num = int(input('Digite um numero (0 - 20): '))
    if num in range(0, 21):
        print(f'Você digitou o número {numeros[num]}.')
        break
    else:
        print('Inválido. Tente novamente. ', end='')