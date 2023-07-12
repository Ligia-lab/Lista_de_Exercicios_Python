# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e a tangente desse ângulo.

import math

ang = float(input('Escolha um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('Com o ângulo {}, temos o seno {:.2f}, cosseno {:.2f} e tangente {:.2f}.'.format(ang, sen, cos, tan))
