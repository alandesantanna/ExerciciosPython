primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{}° termo = {}'.format(cont, termo, end='' ))
        termo += razao
        cont+=1

    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')