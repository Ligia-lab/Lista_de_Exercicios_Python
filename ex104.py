#Crie um programa que tenha a funcao leiaInt(), que vai funcionar de forma semelhante a função input() do Python,
# só que fazendo a validação para aceitas apenas um valor numérico. EX: n = leiaInt('digite um n')


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Digite um numero valido.')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')