# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
# mas com uma validação de dados para aceitar apenas valores que sejam monetários.


def leia_dinheiro(msg):
    """
    trata a entrada de dado para dar mensagem de erro se incorreto
    Args:
        msg: input de um valor em forma de string, que é tratada(, para .; tira os espaços; e se for texto da mensagem de erro)

    Returns: valor formatado

    """
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)
