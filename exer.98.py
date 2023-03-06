def contador():
    for cont in range(1, 11):
        print(cont, end=' ')
    print('Fim! ')


def linha():
    print('=-' * 20)


linha()
print('Contagemde 1 até 10 de 1 em 1.')
contador()
linha()


def retracao():
    for cont in range(10, -1, -2):
        print(cont, end=' ')
    print('Fim !')


print('Contagem de 10 até 0 de 2 em 2.')
print(retracao())
linha()

print('Agora é sua vez de personalizar a contagem !')
def personalize(ini,fim, passo):
    for cont in range(ini, fim, passo):
        print(cont, end=' ')
    print('Fim')
personalize(90, 40, 10)

