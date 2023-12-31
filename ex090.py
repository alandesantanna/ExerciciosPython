ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    media = (nota1 + nota2) / 2  # A média deve ser calculada após a inserção das notas

    ficha.append([nome, [nota1, nota2], media])

    resp = ''
    while resp not in ['S', 'N']:
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if resp not in ['S', 'N']:
            print("Por favor, responda apenas com 'S' para sim ou 'N' para não.")

    if resp == 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"MÉDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
     print('-' * 40)
     opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
     if opc == 999:
         print('Finalizando...')
         break
     if opc <= len(ficha) - 1:
          print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('Volte sempre')