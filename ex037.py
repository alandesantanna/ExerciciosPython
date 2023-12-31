n = int(input('Digite um número inteiro: '))
print('Você digitou o número: {}'.format(n))

conversor = int(input('''escolha a base de conversão
1 - binário
2 - Octal
3 - hexadecimal
Digite um número: '''))

if conversor == 1:
    print('O número {}, em binário é {}'.format(n, bin(n)[2:] ))
elif conversor == 2:
    print('O número {}, em hexadecimal é {}'.format(n, hex(n)[2:] ))
elif conversors == 3:
    print('O número {}, em octal é {}'.format(n, oct(n)[2:] ))
else:
    print('Opção invalida, tente novamente')