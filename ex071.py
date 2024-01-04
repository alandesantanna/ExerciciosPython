lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi pra caramba')

print('')

for c in lanche:
    print(f'Eu vou comer {c}')
print('Comi pra caramba')

print('')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba')

print('')

print(sorted(lanche))

print('')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)

print('')

d = b + a
print(d)
