# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e motre o comprimento da hipotenusa.

'''co = float(input('O cateto oposto mede: '))
ca = float(input('O cateto adjacente mede: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa mede {:.2f}'.format(hi))
'''



'''from math import hypot

co = float(input('O cateto oposto mede: '))
ca = float(input('O cateto adjacente mede: '))
print('A hipotenusa mede: {:.2f}'.format(hypot(co,ca)))'''



import math

co = float(input('O cateto oposto mede: '))
ca = float(input('O cateto adjacente mede: '))
print('A hipotenusa mede: {:.2f}'.format(math.hypot(co,ca)))

