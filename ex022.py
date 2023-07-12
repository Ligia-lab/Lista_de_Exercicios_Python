#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Quantas letras ao no total, sem considerar os espaços
#Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print('maiúsculo:{}'.format(nome.upper()))
print('minúsculo:{}'.format(nome.lower()))
print('a quantidade de caracteres é {}'.format(len(nome) - nome.count(' ')))
#print('o primeiro nome tem {} letras'.format(nome.find(' ')))
separado = nome.split()
print('o primeiro nome é {} e tem {} letras'.format(separado[0], len(separado[0])))