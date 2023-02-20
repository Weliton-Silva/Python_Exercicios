valores = [[], []]
num = 0
pares = impares = 0
for p in range(1, 8):
    num = (int(input(f'Digite o {p}º. valor: ')))
    if num % 2 == 0:
        valores[0].append(num)
    if num % 2 == 1:
        valores[1].append(num)
print('-='*30)
print(f'Os valores pares digitados foram {sorted(valores[0])}')
print(f'Os Valores impares digitados foram {sorted(valores[1])}')
