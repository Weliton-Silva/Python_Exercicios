from time import sleep

print('Sequência de Fibonacci')
sleep(1)
termo = int(input('Primeiro termo'))
termo1 = termo -1
termo2 = termo -2
while termo > 0:
    print('Sequencia {}'.format(termo - termo1 - termo2))
