from random import randint

vtpc = res = npc = vtjd = 0

while True:
    n = int(input('Digite um número: '))
    parImpar = str(input('Escolha Par ou Impar [P/I]')).upper()
    npc = randint(0, 10)

    res = (n + npc)%2
    print(f'O computador escolheu {res}')

    if res == 0 and parImpar == 'P':
        vtjd+=1
        print('Jogador ganhou')

    elif res == 0 and parImpar == 'I':
        vtpc+=1
        print('Jogador perdeu')

    elif res == 1 and parImpar == 'P':
        vtpc += 1
        print('Jogador perdeu')

    elif res == 1 and parImpar == 'I':
        vtjd += 1
        print('Jogador ganhou')

    if vtpc == 3:
        print('O computador ganhou')
        break
    elif vtjd == 3:
        print('O jogador ganhou')
        break
