from math import pow

altura = float(input('Qual a sua altura?: '))
peso = float(input('Qual seu peso?: '))

rz_altura = pow(altura,2)
imc = peso/rz_altura

print('Seu imc é {:.2f}'.format(imc))

if imc<18.5:
    print('Abaixo do peso')
elif imc>=18.5 and  imc<25:
    print('Peso ideal')
elif imc>=25 and imc<30:
    print('Sobrepesso')
elif imc>=30 and imc<40:
    print('Obesidade')
elif imc>40:
    print('Obesidade morbida')