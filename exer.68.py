import random
from random import randint
print('=-'*30)
print('VAMOS JOGAS PAR OU IMPAR')
print('=-'*30)
joga = ''
sorte = random.randint(0, 10)
n1 = 0
cont = 0
compu = sorte
par = (n1 + sorte) % 2 ==0
while True:
    n1 = int(input('Diga um Valor ?'))
    joga = str(input('Par ou impar ?')).upper()[0]
        if joga ==  'P':
            par == True
            print('Você Venceu !')
            cont += 1
        elif joga == 'I':
            par == 1



