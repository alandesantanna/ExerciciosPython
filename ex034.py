sal = float(input('Digite o valor do seu salário: '))

if sal>1250:
    aumento = (10/100)*sal
    novo_sal = sal + aumento
    print('O seu salário de R${:.2f}, aumento em 10%, ficando com o valor de R${:.2f}'.format(sal, novo_sal))
else:
    aumento = (15/100)*sal
    novo_sal = sal + aumento
    print('O seu salário de R${:.2f}, aumento em 15%, ficando com o valor de R${:.2f}'.format(sal, novo_sal))
