matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
total = coluna3 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {l, c}: '))
        if matriz[l][c] % 2 == 0:
            total += matriz[l][c]
print('-='*30)
print(matriz[0])
print(matriz[1])
print(matriz[2])
print('=-'*30)
print(f'A soma de todos valores pares são {total}.')
for l in range(0, 3):
    coluna3 += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {coluna3}.')
print(f'O maior valor da terceira linha é {max(matriz[1])}.')


