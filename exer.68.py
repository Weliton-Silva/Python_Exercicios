import random
from random import randint
print('=-'*30)
print('VAMOS JOGAS PAR OU IMPAR')
print('=-'*30)
n1 = int(input('Diga um Valor: '))
jog = str(input('Par ou Impar ? [P/I]')).upper()[0]
sorte = random.randint(0, 10)
cont = 0
compu = sorte
while True:
     if jog == 'P':
        if (n1 + sorte) % 2 == 0:
            print('Você Venceu !')
    cont += 1
    if jog == 'I':
        if (n1 + sorte) % 2 == 1:
            print('Você Venceu !')
    cont +=1
    if compu
print('Você Perdeu')
