import math
num = int(input('Digite um número: '))
seno = math.sin(math.radians(num))
coseno = math.cos(math.radians(num))
tangente = math.tan(math.radians(num))

print('Seno é {:.2f}, Coseno é {:.2f}, Tangente é {:.2f}'.format(seno, coseno, tangente))

