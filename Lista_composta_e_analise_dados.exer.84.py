pessoas = list()
copias = []
tot = 0
cont = ' '
maior = menor = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append((float(input('Peso: '))))
    if len(copias) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    copias.append(pessoas[:])
    pessoas.clear()
    tot += 1
    cont = str(input('Deseja continuar ?')).upper().split()[0]
    if cont == 'N':
        break
print(maior)
print(f'Foram cadastrados {tot}')
print(f'O maior peso é {maior}Kg.', end=' ')
for p in copias:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso é de {menor}Kg.', end=' ')
for p in copias:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
print()
