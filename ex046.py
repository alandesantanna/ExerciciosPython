from time import sleep

for c in range(11, 0, -1):
    print('número {}'.format(c-1))
    sleep(1)

print('concluido')