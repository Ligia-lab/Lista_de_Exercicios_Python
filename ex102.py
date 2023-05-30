#Crie um programa que tenha uma funcao fatorial() que receba dois parametros:
# o primeiro que indica o numero a calcular e o outro chamado show,
# que será um valor logico (opcional) indicando se sera mostrado ou nao na tela o processo de calculo do fatorial.

def fatorial(num, show=False):
    """
    -> Calcula fatorial de um número
    :param num: número a ser calculado
    :param show: (opcional) mostra ou não a conta
    :return: o valor do fatorial num
    """
    fact = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fact *= c
    return fact


num = int(input('Fatorial de: '))
print(fatorial(num, show=True))
help(fatorial)