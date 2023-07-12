#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.


sexo = input('Informe seu sexo [F/M]: ').strip().upper()[0] #o zero é só pra pegar a primeira letra

while sexo not in 'MmFf':
    sexo = input('Dados inválidos. Informe seu sexo [F/M]: ').strip().upper()[0]
if sexo in 'Mm':
    sexo = 'MASCULINO'
if sexo in 'Ff':
    sexo = 'FEMININO'
print('Sexo {} resgistrado com sucesso.'.format(sexo))