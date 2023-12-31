primeiro = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1

while cont <= 10:
    print('{}° termo = {}'.format(cont, termo ))
    termo += r
    cont+=1

print('FIM')