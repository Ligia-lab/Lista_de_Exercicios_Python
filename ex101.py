#Crie um programa que tenha função chamada voto() que vai receber como parametro o ano de nascimento d uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatprio nas eleições.

def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc
    if idade < 16:
        return f'Você tem {idade} anos: VOTO NEGADO'
    elif idade >= 18 and idade < 65:
        return f'Você tem {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Você tem {idade} anos: VOTO OPCIONAL'


# programa principal
nasc = int(input('Qual seu ano de nascimento: '))
print(voto(nasc))
