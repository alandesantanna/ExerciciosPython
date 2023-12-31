ano_atual = int(input('Digite o ano atual: '))

maior_idade = 0
menor_idade = 0
for c in range(1, 8):
    ano_nascimento= int(input('Qual o ano do seu nascimento? '))
    if ano_atual - ano_nascimento >=18:
        maior_idade+=1
    else:
        menor_idade+=1

print('Maior de idade: {}'.format(maior_idade))
print('Menor de idade: {}'.format(menor_idade))