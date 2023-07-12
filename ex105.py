#Faça um programa que tenha uma função chamada notas() que pode receber varias notas de alunos e vai retornar um dicionario com as seguintes informações:
# -quantidade de notas
# -a maior nota
# -a menor nota
# -a média da turma
# -a situação(opcional)
# Adicione também as docstrings da função.


def notas(*n, sit=False):
    """
    -> Analisa notas dos alunos
    :param n: notas (quantidade ilimitada de notas)
    :param sit: Situação referente à média do aluno (opçional)
    :return: dicionário de notas
    """
    r = {}
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] < 5:
            r['Situação'] = 'RUIM'
        else:
            r['Situação'] = 'RAZOÁVEL'
    return r


# programa principal
resp = notas(8, 5, 0, 6, sit=True)
print(resp)
print()
help(notas)
