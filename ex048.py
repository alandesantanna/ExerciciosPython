s = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        print('Número {}'.format(c))
        s+=c

print('Soma de todos os valores: {}'.format(s))
