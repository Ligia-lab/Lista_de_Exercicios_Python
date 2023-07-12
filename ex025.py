#Crie um programa que leia o nome de uma pessoa e dia se ela tem 'Silva' no nome.

nome = str(input('Insira seu nome completo: ')).strip().title()
print('O nome tem Silva? {}'.format('Silva' in nome))