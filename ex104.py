def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro! Digite um número inteiro válido.')
        if ok:
            break
    return valor


n = leiaInt(f'Digite um número: ')
print(f'Você acabou de digitar um número {n}')
