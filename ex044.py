valor = float(input('Digite o valor do produto: '))
print('Escolha o meio de pagamento: ')
c_pag = int(input('1 - dinheiro/cheque (10% de desconto)\n2 - À vista no cartão(5% de desconto)\n3 - 2x no cartão(preço normal)\n4 - 3x ou mais (20% de juros)\nEscolha umas das opções acima: '))

if c_pag == 1:
    dinheiro_cheque = valor - ((10/100)*valor)
    print('Valor do produto: {}'.format(dinheiro_cheque))
elif c_pag == 2:
    avct = valor -  ((5/100)*valor)
    print('Valor do produto: {}'.format(avct))
elif c_pag == 3:
    print('Valor do produto: {}'.format(valor))
elif c_pag == 4:
    valor_com_juros = valor + ((20/100)*valor)
    print('Valor do produto: {}'.format(valor_com_juros))

