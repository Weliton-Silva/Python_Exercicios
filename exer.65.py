conti = 'S'
n1 = 0
cont = 0
media = 0
maior = 0
menor = 0
while not conti == 'N':
    n1 = int(input('Digite um valor inteiro'))
    cont += 1
    media += n1 / cont
    if n1 >= maior:
        maior = n1
    elif n1 < maior:
        menor = n1
    conti = str(input('Deseja Continuar [S/N] ?')).upper()
print('=-'*20)
print('Final do programa:')
print('=-'*20)
print('''a Média de valores Digitados foi {:.2f}
O maior valor Digitado foi {}
O menor {}'''.format(media, maior, menor))
