n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1+n2)/2

print('A sua média é {:.2f}!'.format(m))

if m >=6:
    print('Parabéns, você passou')
else:
    print('Infelizmente você não passou de ano, estude mais')
print('Até o proximo ano')