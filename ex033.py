n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

if n1 >= n2 and n1 >= n3:
    print('O maior número é o {}'.format(n1))
elif n2 >= n1 and n2 >= n3:
    print('O maior número é o {}'.format(n2))
else:
    print('O maior número é o {}'.format(n3))