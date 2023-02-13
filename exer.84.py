pessoas = list()
copias = []
tot = 0
cont = ' '
maiorp = 0
menorp = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append((int(input('Peso: '))))
    copias.append(pessoas[:])
    pessoas.clear()
    tot += 1
    cont = str(input('Deseja continuar ?')).upper().split()[0]
    if cont == 'N':
        break
print(f'Foram cadastradas {tot} pessoas')
if copias[1] == 0:
    maiorp = menorp = copias[1]
else:
    if copias[1] > maiorp[1]:
        maiorp = copias
    if copias[1] < menorp[1]:
        menorp = copias
print(f'O maior peso foi de {copias[1]}. Peso de {copias[0]}')

