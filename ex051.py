pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
dec = pt + (10-1) * r

for c in range(pt,dec + r, r):
     print('{}'.format(c))
