import os
import random
import turtle
from turtle import clear
import os

print('=-'*20)
print('         Jogo de Adivinhação')
print('=-'*20)
tent = 0
n1 = int(input('Digite um valor de 0 a 10: '))
sorte = random.randint( 0, 10)
while not n1 == sorte:
    print('Tente acerta novamente !')
    n1 = int(input('Digite um valor de 0 a 10: '))
    sorte = random.randint( 0, 10)
    tent = tent + 1
print('Parabéns ! Você acertou,foi Necessario. {} tentativas'.format(tent+1))


