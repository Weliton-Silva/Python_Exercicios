print('-'*40)
print('{:^40}'.format('LOJAS SUPER BARATÃO'))
print('-'*40)
maismil = barato = maior = conta = total = 0
menos = ''

while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    conta += 1
    total += preco
    if preco > 1000:
        maismil += 1
    if conta == 1 or preco < barato:
        barato = preco
        menos = produto
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar ? [S/N]')).upper().split()[0]
    if cont == 'N':
        break
print(f'O Total da compra foi de R${total:.2f}')
print(f'Temos {maismil} custando mais de R$ 1000.00')
print(f'O produto mais barato foi {menos} que custa R${barato:.2f}')
