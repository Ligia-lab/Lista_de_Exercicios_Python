#metros, cm e mm

m = float(input('digite um valor em metros '))
km = m / 1000
cm = m * 100
mm = m * 1000

print('{}km \n{:.0f}cm \n{:.0f}mm'.format(km, cm, mm))
