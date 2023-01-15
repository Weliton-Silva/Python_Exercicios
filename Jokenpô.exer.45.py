from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('=-' * 20)
print('            J O K E N P O')
print('=-' * 20)
print('''Suas Opções:'
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogar = int(input('Qual é a sua jogada: '))
print('=-' * 20)
print('Computador jogou: {}'.format(itens[computador]))
print('Jogador jogou: {}'.format(itens[jogar]))
print('=-' * 20)
if computador == 0:
    if jogar == 0:
        print('Empatamos !')
    elif jogar == 1:
        print('Você Venceu.Parabéns!')
    elif jogar == 2:
        print('Eu Venci.Boa sorte na Proxima !')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:
    if jogar == 0:
        print('Eu Venci.Boa sorte na proxima !')
    elif jogar == 1:
        print('Empatamos !')
    elif jogar == 2:
        print('Você Venceu.Parabéns !')
    else:
        print('JOGADA INVALIDA')
elif computador == 2:
    if jogar == 0:
        print('Você Venceu. Parabéns !')
    elif jogar == 1:
        print('Eu Venci.Boa sorte na Proxima')
    elif jogar == 2:
        print('Empatamos !')
    else:
        print('JOGADA INVALIDA')
