# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# - se ele ainda vai se alistar no serviço militar
# - se é a hora de ele se alistar
# - se já passou do tempo de alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
born = int(input('Em qual ano você nasceu? '))
today = date.today().year
age = today - born
print('Quem nasceu em {} completa {} anos em {}.'.format(born, age, today))
if age == 18:
    print('É hora de se alistar.')
elif age < 18:
    print('Faltam {} anos para se alistar.'.format(18 - age))
    print('Seu alistamento será em {}.'.format(today + (18 - age)))
elif age > 18:
    print('Já deveria ter se alistado há {} anos.'.format(age - 18))
    print('Seu alistamento foi em {}.'.format(today - (age - 18)))
