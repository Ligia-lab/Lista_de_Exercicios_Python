from ex115.lib.interface import *


def arquivoExiste(nome):
    """
    verifica se o arquivo existe
    Args:
        nome: nome do arquivo

    Returns:

    """
    try:
        a = open(nome, 'rt')   # rt = read text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    """
    cria o arquivo, se ele ainda não existir
    Args:
        nome: nome do arquivo

    Returns:

    """
    try:
        a = open(nome, 'wt+')   # wt+ = write text criar
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerArquivo(nome):
    """
    Le o conteudo do arquivo
    Args:
        nome: nome do arquivo

    Returns:

    """
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao abrir o arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')   # separa a linha no ;
            dado[1] = dado[1].replace('\n', '')   # substirui a quebra de linha
            print(f' {dado[0]:<30} {dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    """
    cadastra nova pessoa
    Args:
        arq: nome do arquivo
        nome:  Nome a ser cadastrado
        idade: idade

    Returns:

    """
    try:
        a = open(arq, 'at')   # at = append text
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('Houve um erro ao escrever os dados.')
        else:
            print(f'Novo registro de {nome} cadastrado com sucesso.')
            a.close()

