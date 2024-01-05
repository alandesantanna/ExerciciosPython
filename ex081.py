valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))

    resp = ''
    while resp not in ['S', 'N']:
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if resp not in ['S', 'N']:
            print("Por favor, responda apenas com 'S' para sim ou 'N' para não.")
    if resp == 'N':
        break

print(f'O valores inseridos na fila foram {valores}')
print(f'O tamanho da lista é {len(valores)} ')
valores.sort(reverse=True)
print(f'Essa lista na ordem na ordem decrescente {valores}')

if 5 in valores:
    print('O valor 5 está presente na lista.')
else:
    print('O valor 5 não foi digitado.')