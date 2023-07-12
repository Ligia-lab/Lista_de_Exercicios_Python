# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com sua idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# até 19 anos: JUNIOR
# Até 25 anos: SÊNIOR
# Acima: MASTER

from datetime import date
born = int(input('Digite o seu ano de nascimento: '))
today = date.today().year
age = today- born
if age <= 9:
    print('{} anos é categoria MIRIM.'.format(age))
elif age <= 14:
    print('{} anos é categoria INFANTIL.'.format(age))
elif age <= 19:
    print('{} anos é catergoria JUNIOR.'.format(age))
elif age <= 25:
    print('{} anos é categoria SÊNIOR.'.format(age))
else:
    print('{} anos é categoria MASTER.'.format(age))