from random import randint

joga = {'jogador1',
         'jogador2',
         'jogador3',
         'jogador4'}
sorte = randint(1, 6)
print('Valores Sorteados:')
print('=-'*15)
for j in joga:
    print(f'O {j} tirou {sorte}')
    sorte = randint(1, 6)