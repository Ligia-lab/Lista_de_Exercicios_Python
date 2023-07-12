# Crie um modulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro(), metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.


def aumentar(preço, taxa):
    res = (preço * (taxa / 100)) + preço
    return res


def diminuir(preço, taxa):
    res = preço - (preço * (taxa / 100))
    return res


def dobro(preço):
    res = preço * 2
    return res


def metade(preço):
    res = preço / 2
    return res
