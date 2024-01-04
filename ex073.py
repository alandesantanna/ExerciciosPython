tabela = ('Botafogo', 'Flamengo', 'internacional', 'Atletico', 'São Paulo',
          'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Ceará', 'Atletico',
          'Corinthians', 'Vasco', 'Bahia', 'Sport', 'Coritiba', 'Goias', 'Barcelona',
          'Chapecoense', 'Argentina')

while True:
    escolha = str(input('Escolha uma das opções\n'
                        'A) Apenas os 5 primeiros\n'
                        'B) Os ùltimos 4 colocados da tabela\n'
                        'C) Uma lista com os time em ordem alfabética\n'
                        'D) Em que posição na tabela está o time da Chapecoense\n'
                        'E) Sair\n')).strip().upper()[0]

    if escolha == 'A':
        for c in range(0, 5):
            print(f'{c+1}° colocado: {tabela[c]}')

    elif escolha == 'B':
        for c in range(-4, 0):
            print(f'{len(tabela) + c + 1}̣° colocado: {tabela[c]}')

    elif escolha == 'C':
        print(sorted(tabela))

    elif escolha == 'D':
        posicao = tabela.index('Chapecoense') + 1
        print(f'O time da Chapecoense tá na posição {posicao}')

    elif escolha == 'E':
        print('Encerramento do programa...')
        break
        