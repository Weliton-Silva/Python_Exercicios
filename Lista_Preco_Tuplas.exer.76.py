listagem = ('Lapis', 1, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidos', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Caneta', 22.30, 'Livro', 34.90)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for cont in range(0, len(listagem)):
    if cont % 2 == 0:
        print(f'{listagem[cont]:.<30}', end='')
    else:
        print(f'R${listagem[cont]:>7.2f}')
