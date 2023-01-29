n1 = 999
cont = valor1 = valor = 0
print('Digite um valor inteiro ou [ 999 ] para sair: ')
while not valor == 999:
    valor = int(input('Digite um valor inteiro: '))
    cont += 1
    valor1 = valor + valor1
print('''Foram Digitados {} valores.
A Soma entre os valores Digitados são {}'''.format(cont - 1, valor1 - 999))
