valores = list()
pares = list()
impares = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = ''
    while resp not in ['S', 'N']:
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if resp not in ['S', 'N']:
            print("Por favor, responda apenas com 'S' para sim ou 'N' para não.")
    if resp == 'N':
        break

for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'O valores inseridos na fila foram {valores}')
print(f'O valores pares inseridos na fila foram {pares}')
print(f'O valores impares inseridos na fila foram {impares}')