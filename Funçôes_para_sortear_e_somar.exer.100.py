from random import randint
from time import sleep

numeros = list()


def sorteio(lista):
    print(f'Sorteando 5 valores da lista:')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ')
        sleep(0.3)
    print('Fim !')
    print('-'*30)



def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


sorteio(numeros)
sleep(0.5)
somaPar(numeros)