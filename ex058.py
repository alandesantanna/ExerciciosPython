n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))

c = 0

while c != 5:
    print('[1] - Somar\n[2] - Multiplicar\n[3] - Maior\n[4] - Novos números\n[5] - Sair do programa')
    c = int(input('Escolha uma opção: '))

    if c == 1:
        s = n1+n2
        print('A soma é:', s)

    elif c == 2:
        m = n1*n2
        print('A multiplicação é:', m)

    elif c == 3:
        if n1>n2:
            print('O número {} é maior'.format(n1))
        elif n2>n1:
            print('O número {} é maior'.format(n2))
        else:
            print('Os números são iguais')

    elif c == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite um valor: '))

print('FIM')