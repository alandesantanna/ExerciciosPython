def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
            continue
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
            continue
        else:
            return n


n1 = leiaInt(f'Digite um número: ')
n2 = leiaFloat(f'Digite um número: ')
print(f'Você acabou de digitar um número inteiro {n1}')
print(f'Você acabou de digitar um número real {n2}')
