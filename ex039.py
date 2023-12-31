ano_nasc = int(input('Digite o ano do seu nascimento: '))
ano_at = int(input('Digite o ano atual: '))

idade = ano_at - ano_nasc

if idade<18:
    print('Ainda vai se alistar')
    print('Falta {} anos'.format(18 - idade))
elif idade==18:
    print('Hora de se alistar')
elif idade>18:
    print('Já passou da hora de se apresentar')
    print('passou {} anos'.format(idade - 18))