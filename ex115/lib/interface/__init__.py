# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter duas opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.


def leiaInt(msg):
    """
    Lê um numero inteiro
    Args:
        msg: sua opção

    Returns: numero escolhida do menu

    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário')
            return 0
        else:
            return n


def linha(tam=42):
    """
    linha para o menu
    Args:
        tam: padrão 42

    Returns: linha vezes o tamanho

    """
    return '-' * tam


def cabeçalho(txt):
    """
    cabeçalho para o menu
    Args:
        txt: titulo do menu

    Returns:

    """
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    """
    Menu propriamente dito
    Args:
        lista: argumentos com as opções do menu

    Returns: opção escolhida

    """
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc


