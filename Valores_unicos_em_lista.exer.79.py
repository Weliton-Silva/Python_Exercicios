valor = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in valor:
        valor.append(n)
    else:
        print('Valor Duplicado ! Não vou adicionar.')
    r = input('Deseja continuar ? [S/N] ').upper().split()[0]
    if 'N' in r:
        break
print(f'Os valores Digitados foram {sorted(valor)}')
