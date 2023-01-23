sexo = ''
M = 0
F = 0
while not sexo == 'M' and 'F':
    sexo = str(input('Digite seu sexo [M/F]: ').upper())
    if sexo == 'F':
        print('Seu Sexo é feminino')
    if sexo == 'M':
        print('Seu Sexo é Masculino')
print('Fim do exercicio')
