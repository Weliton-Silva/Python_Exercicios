from time import sleep

print('Sequência de Fibonacci')
sleep(1)
termo = int(input('Quantos termos você gostaria de mostrar ? '))
termo1 = 0
termo2 = 1
print('{} - {} '.format(termo1, termo2), end='')
cont = 3
while cont <= termo:
    termo3 = termo1 + termo2
    print('- {} '.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    cont += 1
print('FIM')





