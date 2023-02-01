menos20 = maior18 = homens = 0

while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'F' and idade < 20:
        menos20 += 1
    elif idade >= 18:
        maior18 += 1
    elif sexo == 'M':
        homens += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja Continuar ? ')).upper().strip()[0]
    if cont == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {menos20} mulheres com menos de 20 anos.')

