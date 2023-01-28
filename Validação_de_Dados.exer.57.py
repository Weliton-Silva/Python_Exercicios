sexo = ''
M = ''
F = ''
while not sexo == 'M' and 'F':
    sexo = str(input('Digite seu sexo [M/F]: ').upper()).strip()[0]
    if sexo == 'F':
        print('Seu Sexo é feminino')
    elif sexo == 'M':
        print('Seu Sexo é Masculino')
    else:
        print('Dados Invalidos.')
print('Fim do exercicio')
