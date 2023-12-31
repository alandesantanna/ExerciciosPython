maior_peso = menor_peso = float(input('Digite o peso da 1ª pessoa: '))

for c in range(2, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))

    if peso > maior_peso:
        maior_peso = peso

    if peso < menor_peso:
        menor_peso = peso

print('O maior peso é {}'.format(maior_peso))
print('O menor peso é {}'.format(menor_peso))

