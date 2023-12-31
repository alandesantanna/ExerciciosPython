km = float(input('Digite quantos kms deseja viajar: '))

if km<=200:
    v_viagem = km*0.50
    print('Sua viagem de {:.2f} quilômetros vai custar R${:.2f}'.format(km, v_viagem))
else:
    v_viagem = km*0.45
    print('Sua viagem de {:.2f} quilômetros vai custar R${:.2f}'.format(km, v_viagem))