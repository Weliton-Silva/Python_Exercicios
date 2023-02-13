completa = list()
impar = list()
par = list()
cont = ' '

while cont not in 'NS':
    while True:
        n1 = int(input('Digite um valor inteiro: '))
        completa.insert(0, n1)
        cont = str(input('Deseja continuar ?[S/N] ')).upper().split()[0]
        if cont == 'N':
            break
print('=-'*20)
print(f'A lista completa é {completa}')
for c in completa:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
