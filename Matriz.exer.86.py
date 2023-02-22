matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input((f'Digite um valor para {l, c}: ')))
print(('=-'*30))
print(matriz[0])
print(matriz[1])
print(matriz[2])
