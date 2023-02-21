from random import randint
from time import sleep

print('-'*30)
print(f'      JOGO DA MEGA SENA')
print('-'*30)
sorteio = randint(1, 60)
palp = int(input('Quantos jogos deseja fazer ? '))
lista = list()
tot = 1
jogo = list()
while tot <= palp:
    cont = 0
    while True:
        sorteio = randint(1, 60)
        if sorteio not in jogo:
            jogo.append(sorteio)
            cont +=1
        if cont >= 6:
            break
    tot += 1
    jogo.sort()
    lista.append(jogo[:])
    jogo.clear()
print('-='*3, f'SORTEANDO {palp} JOGOS', '-='*3)
for i, l in enumerate(lista):
    print(f'jogo {i+1}: {l}')
    sleep(1)
print('-='*5, 'BOA SORTE', '-='*5)
