from time import sleep
n1 =0
val = 0
val2 = 0

val = int(input('Digite o primeiro valor: '))
val2 = int(input('Digite o segundo valor: '))
sleep(0.5)

while not 5 <= n1:
    sleep(1)
    print('''Menu Inicial:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Numeros
    [ 5 ] Sair do Programa''')
    n1 = int(input('Digite a opção desejada: '))
    if n1 == 1:
        print('A Soma dos valores é {}'.format(val + val2))
    elif n1 == 2:
        print('a Multiplicação de ambos valores é {}'.format(val * val2))
    elif n1 == 3:
        if val > val2:
            print('O primeiro valor {} é o maior'.format(val))
        elif val < val2:
            print('O Segundo valor {} é o maior'.format(val2))
        else:
            print('Valorea digitados são iguais.')
    elif n1 == 4:
        print('Digite novos Valores.')
        val = int(input('Digite o primeiro valor: '))
        val2 = int(input('Digite o segundo valor: '))
        sleep(1)
    if n1 == 5:
        sleep(1)
        print('Fim do programa.')
    else:
        print('Opção Invalida.Tente Novamente')
