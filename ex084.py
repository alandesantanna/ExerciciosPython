temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = ''
    while resp not in ['S', 'N']:
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if resp not in ['S', 'N']:
            print("Por favor, responda apenas com 'S' para sim ou 'N' para não.")
    if resp == 'N':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas. ')
print(f'O maior peso foi de {mai}kg. Peso de ', end='')
for p in princ:
    if  p[1] == mai:
        print(f' {p[0]} ')
print(f'O menor peso foi de {men}kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f' {p[0]} ', end='')
print()