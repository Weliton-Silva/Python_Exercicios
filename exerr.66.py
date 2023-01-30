cont = soma = 0
while True:
    n1 = int(input('Digite um valor Inteiro: '))
    if n1 == 999:
        break
    soma += n1
    cont += 1
print('=-'*20)
print('Fim de Programa')
print('=-'*20)
print(f'A soma dos {cont} valores é {soma}! ')
