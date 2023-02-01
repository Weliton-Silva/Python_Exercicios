print('-'*30)
print('LOJAS SUPER BARATÃO')
print('-'*30)
total = 0
maismil = 0
barato = 0
menos = 0
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    if preco > 0:
        total = total + preco
    if preco > 1000:
        maismil += 1
    #if preco > barato:

    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar ? [S/N]')).upper().split()[0]
    if cont == 'N':
        break
print(f'O Total da compra foi de R${total:.2f}')
print(f'Temos {maismil} custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R${menos:.2f}')
