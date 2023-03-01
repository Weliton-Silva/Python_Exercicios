from random import randint
from time import sleep
from operator import itemgetter

joga = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
rank = list()
print('Valores Sorteados:')
print('=-'*15)
for j, v in joga.items():
    print(f'O {j} tirou {v} no dado.')
    sleep(1)
print('=-'*15)
print('=='*2, 'RANGING DOS JOGADORES', '=='*2)
rank = sorted(joga.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(rank):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
print('Fim da partida')
