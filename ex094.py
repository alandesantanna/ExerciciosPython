jogador = dict()
partidas = list()

jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(0, tot):
    gols_partida = int(input(f'Quantidade de gols na partida {c + 1}? '))
    partidas.append(gols_partida)

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print(jogador)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f' => Na partida {i + 1}, fez {v} gols')  # Adicionei +1 para corrigir a numeração da partida
print(f'Foi um total de {jogador["total"]} gols.')