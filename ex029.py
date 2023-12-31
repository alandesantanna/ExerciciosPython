vel = float(input('Digite a velocidade do carro: '))

if vel >= 80:
    print('Velocidade acima do permitido')
    v_multa = (vel - 80) * 7
    print('Velocidade: {} \nO valor da multa é R${:.2f}'.format(vel, v_multa))
else:
     print('Velocidade permitada pela via')