#Crie um programa que leia idade e o sexo de várias pessoas.
# A cada pessoa cadastrada o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B)quantos homens foram cadastrados
# C) quantas mulheres tem menos de 20 anos

idade = 0
sexo = ' '
mais18 = 0
homem = 0
mulher_menos_20 = 0

while True:
    print('-=' * 20)
    idade = int(input('Insira sua idade: '))
    sexo = str(input('Insira seu sexo [F/M]: ')).upper().strip()[0]

    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F':
        if idade < 20:
            mulher_menos_20 += 1

    if sexo not in 'FM':
        print('Inválido. Tente novamente')
    else:
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if continuar in 'N':
            print('Finalizando...')
            break

print(f'A) {mais18} pessoas tem mais de 18 anos.')
print(f'B) {homem} homens foram cadastrados.')
print(f'C) {mulher_menos_20} mulheres tem menos de 20 anos.')
print('FIM')
