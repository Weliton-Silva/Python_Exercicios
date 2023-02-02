import random
from random import randint

print('='*30)
print('BANCO CEV')
print('='*30)
valor = int(input('Que valor você quer sacar ? R$'))
saque = 0
cel50 = 50
cel20 = 20
cel10 = 10
cel1 = 1
n1 = n2 = n3 = n4 = 0
while not valor == saque:
    if valor >= saque:
        saque = saque + cel50
        n1 += 1
        if valor == saque:
            print(f'Total de {n1} cédulas de R$ 50,00')
    elif valor >= saque:
        saque = saque + cel20
        n2 += 1
        if valor == saque:
            print(f'Total de {n2} cédulas de R$ 20,00')
    elif valor >= saque:
        saque = saque + cel10
        n3 += 1
        if valor == saque:
            print(f'Total de {n3} cédulas de R$ 10,00')
    elif valor >= saque:
        saque = saque + cel1
        n4 += 1
        if valor == saque:
            print(f'Total de {n4} cédulas de R$ 1,00')
print('='*30)
print('Volte sempre ao BANCO CEV ! Tenha um ótimo dia.')
