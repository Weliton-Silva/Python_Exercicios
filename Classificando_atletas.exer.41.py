from datetime import date
idade = int(input('Data de Nascimento: '))
ano = date.today().year - idade
if ano <= 9:
    print('Você tem {} anos.'.format(ano))
    print('CATEGORIA: MIRIM')
elif ano <= 14:
    print('Você tem {} anos.'.format(ano))
    print('CATEGORIA :INFANTIL')
elif ano <= 19:
    print('Você tem {} anos.'.format(ano))
    print('CATEGORIA: JUNIOR')
elif ano <= 25:
    print('Você tem {} anos.'.format(ano))
    print('CATEGORIA: SÊNIOR')
else:
    print('Você tem {} anos.'.format(ano))
    print('CATEGORIA: MASTER')
