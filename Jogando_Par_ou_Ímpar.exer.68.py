from random import randint

print('=-'*30)
print('VAMOS JOGAS PAR OU IMPAR')
print('=-'*30)
cont = 0
while True:
    jogador = int(input('Diga um Valor: '))
    sorte = randint(0, 10)
    soma = jogador + sorte
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar ? [P/I] ')).upper().strip()[0]
    print(f'Jogador Jogou {jogador} e o computador {sorte}. Total de {soma}')
    print('Deu Par.'if soma % 2 == 0 else 'Deu Impar.')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você Venceu !')
            cont += 1
        elif soma % 2 == 1:
            print('Você Perdeu')
            break
    if tipo == 'I':
        if soma % 2 == 1:
            print('Você Venceu')
            cont += 1
        elif soma % 2 == 0:
            print("Você Perdeu !")
            break
print('=-'*30)
print(f'GAME OVER !Você Venceu {cont}vezes.')




