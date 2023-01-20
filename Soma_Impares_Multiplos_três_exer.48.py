print('Soma impares multiplos de 3 ate 500')
soma = 0
for n in range(3, 501, 3):
    if n % 2 == 1:
        soma = soma + n
print('Valor total é {}'.format(soma))
