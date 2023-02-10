valor = 0
lista = list()
cont = ''
if valor != lista:
    lista = valor
else:
    print('Valor duplicado')
    while cont not in 'N':
        valor = int(input('Digite um valor: '))
        cont = str(input('Deseja continuar ? ')).upper()
    print(lista.sort())
