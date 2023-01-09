import random
n1 = int(input('Digite um numero 0 a 10...'))
sorte = random.randint(0, 10)
print('Pensando....')
if n1 == sorte:
    print('Parabens você acertou !')
else:
    print('Mais sorte na proxima ! Você errou.')

