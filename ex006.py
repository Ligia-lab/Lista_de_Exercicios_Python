#nº, dobro, triplo e raiz quadrada

n = int(input('escolha um numero: '))
nd = n * 2
nt = n * 3
nr = n ** (1/2)

print('o dobro de {} é {}, o triplo é {}, e a raiz quadrada é {:.2f}.'.format(n, nd, nt, nr))
