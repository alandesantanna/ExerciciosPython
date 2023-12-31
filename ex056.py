sexo = str(input('Digite seu sexo (M/F): ')).upper()

while sexo != 'M' and sexo != 'F':
    print("Valor incorreto! Digite 'M' para masculino ou 'F' para feminino.")
    sexo = input("Digite novamente o sexo (M/F): ").upper()

if sexo == 'M':
    print('Sexo escolhido: Masculino')
if sexo == 'F':
    print('Sexo escolhido: Feminimo')
