valor = list()

for cont in range( 0, 5):
    n1 = int(input('Digite um valor: '))
    if cont == 0 or n1 > valor[-1]:
        valor.append(n1)
    else:
        pos = 0
        while pos < len (valor):
            if n1 <= valor[pos]:
                valor.insert(pos, n1)
                break
            pos += 1
print(f'Os valores digitados em ordem foram {valor}')