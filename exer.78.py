n1 = list()
maior = 0
menor = 0
for cont in range(0, 5):
    n1.append(int(input(f'Digite um valor para posição {cont}: ')))
    if cont == 0:
        maior = menor = n1[cont]
    else:
        if n1[cont] > maior:
            maior = n1[cont]
        if n1[cont] < menor:
            menor = n1[cont]
print(f'Você digitou os valores {n1}')
print(f'O maior valor digitado foi {maior} na posição ', end='')
for cont, v in enumerate(n1):
    if v == maior:
        print(f'{cont}...', end='')
print()
print(f'O menor valor digitado foi {menor} na posição ', end='')
for cont2, v in enumerate(n1):
    if v == menor:
        print(f'{cont2}...', end='')
