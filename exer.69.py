print('-'*20)
print('CADASTRE UMA PESSOA')
print('-'*20)
sexo = ' '
cont = ' '
menos20 = 0
maior18 = 0
homens = 0
while sexo not in 'FM':
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'F':
        if idade <= 20:
            menos20 += 1
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        homens += 1
    cont = str(input('Quer Continuar ? [S/N] ')).strip().upper()[0]
if cont == 'S':
    print('Cadastre uma Pessoa')
if cont =='N':
    print('Fim de Programa')
    break

print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {menos20}mulheres com menos de 20 anos.')

