# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um numero de tipo inválido.
# Aproveite e crie tambem uma funçaõ leiaFloat() com a mesma funcionalidade.


def leiaInt(msg):
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


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg).replace(',', '.'))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário')
            return 0
        else:
            return n


n = leiaInt('Digite um número inteiro: ')
nf = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número {n} e {nf}'.replace('.', ','))