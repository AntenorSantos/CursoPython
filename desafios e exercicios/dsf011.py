l = float(input('Qual a largura da parede? '))
a = float(input('Qual a altura da parede? '))
area = l * a
print('Sua parede tem a dimensão de {}m x {}m e sua área é de {}m². '.format(l, a, area))
tinta = area / 2
print('Para pintar essa parede, você precisara de {}l litros de tinta'.format(tinta))