#qual a área da parede e quantos litros de tinta são necessários pra pintar, sendo que cada litro pinta 2m²?

a = float(input('qual a altura da parede? '))
l = float(input('qual a largura da parede? '))
area = a * l
tinta = area/2
print('a área da parede é {:.1f}m², e serão necessários {:.1f}L de tinta'.format(area, tinta))

