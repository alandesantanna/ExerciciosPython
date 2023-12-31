dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos kilometros rodados? '))
vt = (dias * 60) + (km * 0.15)

print('Valor total: R${:.2f}'.format(vt))
