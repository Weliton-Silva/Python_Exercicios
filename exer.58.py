import random

print('=-'*20)
print('         Jogo de Adivinhação')
print('=-'*20)
sorte = random.randint( 0, 10)
acertou = False
tent = 0
while not acertou:
    n1 = int(input('Qual é o seu palpite ? '))
    tent += 1
    if n1 == sorte:
        acertou = True
    else:
        if n1 < sorte:
            print('Mais... Tente Novamente.')
        elif n1 > sorte:
            print('Menos... Tente Novamente.')
print('Parabéns ! Você acertou,foi Necessario. {} tentativas'.format(tent))
