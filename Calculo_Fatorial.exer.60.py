import math
n1 = int(input('Digite o numero que deseja saber o seu Fatorial: '))
cont = 'S'
if n1 < 2:
    print('Não formara Fatorial.')
elif n1 >= 2:
        print('O Fatorial de {} é {}'.format(n1, math.factorial(n1)))
