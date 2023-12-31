from random import randint
n = int(input('Digite um número: '))
numero_aleatorio = 0
qtd_palpites = 0
while n != numero_aleatorio:
    numero_aleatorio = randint(0, 10)
    print('Errado! a resposta certa era {}'.format(numero_aleatorio))
    n = int(input('Digite um número: '))
    qtd_palpites +=1
print('acertou!')
print('foi necessário {} palpites para acerta'.format(qtd_palpites))