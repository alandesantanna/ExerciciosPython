a = float(input('Digite o tamanho do lado A do triangulo: '))
b = float(input('Digite o tamanho do lado B do triangulo: '))
c = float(input('Digite o tamanho do lado C do triangulo: '))

if (a + b > c) and (b + c > a) and (a + c > b):
    print('Pode ser um triangulo')
    if a == b == c:
        print('Triangulo equilatero')
    elif a == b or b == c or c == a:
        print('Triangulo isósceles')
    elif a != b and b != c and c != a:
        print('Triangulo escaleno')
else:
    print('Não poder ser triangulo')
