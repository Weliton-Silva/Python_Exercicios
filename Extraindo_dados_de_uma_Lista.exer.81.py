valor = list()
contador = 0
prox = ' '
while prox not in 'SN':
    while True:
        n1 = int(input('Digite um valor: '))
        valor.append(n1)
        contador += 1
        prox = str(input('Deseja continuar ? [S/N]')).upper().strip()[0]
        if prox == 'N':
            break
print('=-'*30)
print(f'Foram digitados {contador} valores.')
print(f'Os valores digitados em ordem decrescente são {sorted(valor, reverse=True)}')
if valor.count(5) == True:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
