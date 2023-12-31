nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')

print('Seu nome em maiúsculo fica: {}'.format(nome.upper()))
print('Seu nome em minusculo fica: {}'.format(nome.lower()))

print('Seu nome tem no total {} caracteres: '.format(len(nome) - nome.count(' ')))

print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))