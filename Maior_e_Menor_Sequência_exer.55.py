menor = 0
maior = 0
for c in range(1, 6):
    peso = float(input('Digite o seu peso(Kg): '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso em Kg digitado foi {:.1f}Kg.E o menor {:.1f}Kg.'.format(maior, menor))
