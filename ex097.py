def area(l, c):
    a = l * c
    print(f'A area do terreno {l}x{c} é {a:0.2f} metros quadrados')


largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))

area(largura, comprimento)
