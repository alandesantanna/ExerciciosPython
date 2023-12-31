n = 0
s = n
cont = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    cont += 1

print('A soma de todos os valores digitados é {}'.format(s))
print('Foram digitados {} números'.format(cont))