largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area_parede = largura*altura

print('Cada litro de tinta pinta um area de 2 metros quadrados')

qtd_tinta = area_parede/2

print('vc vai precisar de {} litros de tinta para pintar {} metros, que é a área da parede'.format(qtd_tinta, area_parede))