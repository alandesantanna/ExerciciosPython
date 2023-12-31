print('Calculadora de soma entre dois valores')
n1 = float(input('Digite um valor inteiro: '))
n2 = float(input('Digite um segundo valor inteiro: '))
som = n1+n2
sub = n1-n2
mult = n1*n2
div = n1/n2
pot = n1**n2
div_inteira = n1//n2
rest_div = n1%n2
print('A soma entre {} e {} é {}'.format(n1, n2, som))
print('A subtração entre {} e {} é {}'.format(n1, n2, sub))
print('A multiplicação entre {} e {} é {}'.format(n1, n2, mult))
print('A divisão entre {} e {} é {}'.format(n1, n2, div))
print('A potência entre {} e {} é {}'.format(n1, n2, pot))
print('A divisão inteira entre {} e {} é {:.2f}'.format(n1, n2, div_inteira))
print('O resto da divisão entre {} e {} é {}'.format(n1, n2, rest_div))