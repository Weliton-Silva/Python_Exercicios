n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
valores = n1, n2, n3, n4
valor9 = 0
posicao3 = 0
pares = 0
print(f'Você Digitou os valores {valores}')
for cont in valores:
    if cont == 9:valor9 += 1
    if cont % 2 == 0:
        pares += 1
    posicao3 += 1
print(f'O número 9 e digitado {valor9} vezes.')
print(f'O número 3 aparece {posicao3} posição')
print(f'Os valores pares digitados foram {pares}')


