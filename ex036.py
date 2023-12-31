v_casa = float(input('Valor da casa: '))
sal = float(input('Digite o salário do comprador: '))
qtd_meses = int(input('Em quantos meses deseja pagar: '))

v_mensal = v_casa/qtd_meses
por_sal = (30/100)*sal

if v_mensal>=por_sal:
    print('O valor das parcelas ficaram em R${:.2f}, \ninfelizmente a comprar foi negado '.format(v_mensal))
else:
    print('Sua compra foi feia com sucesso. \nSuas parcelas ficaram apenas R${:.2f}'.format(v_mensal))
