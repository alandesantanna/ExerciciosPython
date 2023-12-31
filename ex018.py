from random import choice

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

nomes = [n1, n2, n3, n4]

psa_aleatoria = choice(nomes)

print('pessoa aleatoria: {}'.format(psa_aleatoria))
