# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter duas opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Listar pessoas', 'Cadastrar pessoa',  'Sair'])
    if resposta == 1:
        # Lista o conteúdo do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Cadastra uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema....')
        break
    else:
        print('\033[31mERRO: Digite uma opção válida.\033[m')
    sleep(1)