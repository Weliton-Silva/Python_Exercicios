from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += p
        print('Fim !')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= p
        print('Fim !')


def linha():
    print('=-'*20)


linha()
contador(1, 10, 1)
linha()
contador(10, 0, 2)
linha()
print('Agora é sua vez de personalizar a contagem !')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Pulando: '))
sleep(0.5)
linha()
contador(ini, fim, pas)
linha()
