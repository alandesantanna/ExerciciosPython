a = float(input('Digite o tamanho do lado A do triangulo: '))
b = float(input('Digite o tamanho do lado B do triangulo: '))
c = float(input('Digite o tamanho do lado C do triangulo: '))

if (a + b > c) and (b + c > a) and (a + c > b):
    print('Pode ser um triangulo')
else:
    print('Não poder ser triangulo')
