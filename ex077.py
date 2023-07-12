# Crie um programa que tenha uma tupla com varias palavras(não usar acento).
# Depois disso você deve mostrar para cada palavra quais são suas vogais.

palavras = ('caneta', 'caderno', 'mochila', 'estojo', 'cerveja')

for cont in palavras:
    print(f'\nNa palavra "{cont.upper()}" temos ', end='')
    for letra in cont:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')