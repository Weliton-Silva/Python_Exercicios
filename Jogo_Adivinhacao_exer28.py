import random
n1 = int(input('Digite um numero 0 a 10...'))
sorte = random.randint(0, 10)
print('-'*20)
print('Pensando....')
print('-'*20)
print('Pensei no número {} você Digitou {}'.format(sorte, n1))
if n1 == sorte:
    print('Parabens você acertou !')
else:
    print('Mais sorte na proxima ! Você errou.')
