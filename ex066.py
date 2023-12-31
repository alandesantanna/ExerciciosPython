n = res = 0
while True:
    n = int(input('Digite um número: '))
    if n < 0:
        break

    for c in range(0, 10):
        c+=1
        res=n*c
        print(f'{n} X {c} = {res}')
print('FIM')