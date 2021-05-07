larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
tinta = area / 2

print('Dimensão parede de {}x{} e área de {}m². '.format(larg, alt, area))
print('Tinta necessária para pintar a parede: {} litros. '.format(tinta))


