from random import randint

num = int(input('Digite um número entre 0 e 5: '))
numRandom = randint(0, 5)

if num == numRandom:
    print('Parabéns, você acertou o número')
else:
    print('Você digitou o número errado! \nVocê escolheu o número {} \nO programa escolheu o número {}'.format(num, numRandom))
