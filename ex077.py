lista = ('aprender', 'programar', 'treinar', 'estudar',
         'python', 'curso', 'gratis', 'praticar', 'trabalhar',
         'mercado', 'futuro', 'linguagem')

for p in lista:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')