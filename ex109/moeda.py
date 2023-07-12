# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvido no desafio 108.


def aumentar(preço=0, taxa=0, formato=False):
    """
    Aumento do valor
    Args:
        preço: valor
        taxa: porcentagem de aumento
        formato: formato de exibição, como dinheiro ou não, padrão False

    Returns: valor com aumento

    """
    res = (preço * (taxa / 100)) + preço
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    """
    desconto no valor
    Args:
        preço: valor original
        taxa: porcentagem de desconto
        formato: normal ou em forma de moeda, padrão flase

    Returns:valor com desconto

    """
    res = preço - (preço * (taxa / 100))
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    """
    dobro do valor
    Args:
        preço: valor
        formato: formatado ou não. padrão false

    Returns: dobro do valor

    """
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    """
    metade do valor
    Args:
        preço: valor
        formato: formatado ou não, padrão false

    Returns:metade do valor

    """
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    """
    formatação do valor, com subtituição do ponto por virgula
    Args:
        preço: valor
        moeda: moeda desejada (não converte), padrão R$

    Returns: valor formatado

    """
    return f'{moeda}{preço:.2f}'.replace('.', ',')

