from time import sleep

print('Sequência de Fibonacci')
sleep(1)
termo = int(input('Primeiro termo'))
termo1 = 0
termo2 = 1
fb = 0

while fb == 15:
    if fb >= termo1:
        print('Fibonacci {}'.format(fb+termo1))
        termo2 = +1
else:
    termo1 = termo2 + fb
    print('Fibonacci {}'.format(termo1))



