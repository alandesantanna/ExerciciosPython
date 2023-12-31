ano_nasc = int(input('Digite seu ano de nascimento: '))
ano_at = int(input('Digite ano atual: '))

idade = ano_at - ano_nasc
print('Sua idade atual é: {}'.format(idade))
if idade<=9:
    print('Mirim')
elif idade>9 and idade<=14:
    print('Infantil')
elif idade>14 and idade<=19:
    print('Junior')
elif idade>19 and idade<=20:
    print('Senior')
elif idade>20:
    print('Master')