matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
total = 0
linha = coluna = 0
for l in range(0, 3):
    linha += l
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {l, c}: '))
        coluna += c

print('-='*30)
print(matriz[0])
print(matriz[1])
print(matriz[2])
print('=-'*30)
total = sum(matriz)
print(f'A soma de todos valores são {total}')
print(f'')
print(f'O maior valor da terceira linha é {max(matriz[1])}.')


