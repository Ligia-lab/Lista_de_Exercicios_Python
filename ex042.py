# Refaça o exercício 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isóceles: dois lados iguais
# Escaleno: todoa os lados diferentes

r1 = float(input('Insira o valor da primeira reta: '))
r2 = float(input('Insira o valor da segunda reta: '))
r3 = float(input('Insira o valor da terceira reta: '))
if (r1 + r2 > r3) and (r2 + r3 > r1) and (r3 + r1 > r2):
    print('PODE formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO.')
    elif r1 != r2 != r3 !=r1:
        print('ESCALENO.')
    else:
        print('ISÓCELES.')
else:
    print('NÃO PODE formar um triângulo.')

'''r1 = float(input('Insira o valor da primeira reta: '))
r2 = float(input('Insira o valor da segunda reta: '))
r3 = float(input('Insira o valor da terceira reta: '))
t = ''
if (r1 + r2 > r3) and (r2 + r3 > r1) and (r3 + r1 > r2):
    t = True
else:
    print('NÃO PODE formar um triângulo.')
if t == True and r1 != r2 and r2 != r3:
    print('PODE formar um triângulo ESCALENO')
elif t == True and r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
    print('Pode formar um triângulo ISÓCELES')
elif t == True and r1 == r2 == r3:
    print('Pode formar um triângulo EQUILÁTERO')'''





'''
if (r1 + r2 > r3) and (r2 + r3 > r1) and (r3 + r1 > r2) and r1 != r2 and r2 != r3:
    print('PODE formar um triângulo ESCALENO')
elif (r1 + r2 > r3) and (r2 + r3 > r1) and (r3 + r1 > r2) and r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
    print('Pode formar um triângulo ISÓCELES')
elif (r1 + r2 > r3) and (r2 + r3 > r1) and (r3 + r1 > r2) and r1 == r2 == r3:
    print('Pode formar um triângulo EQUILÁTERO')
else:
    print('NÃO PODE formar um triângulo.')'''