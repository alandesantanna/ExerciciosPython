from time import sleep
def maior(* num):
    cont = maior = 0
    print('=' * 30)
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)

        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


#Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(3, 4, 5, 0)
maior(5, 2, 7, 3, 8, 7)
maior(6)
maior()