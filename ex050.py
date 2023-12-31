s = 0
for c in range(0, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s+=n

print('A soma de todos os valores pares digitados é: {}'.format(s))