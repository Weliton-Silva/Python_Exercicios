ano = int(input('Digite o Ano desejado: '))
if ano % 4 == 0:
    print('{} é um ano Bissexto'.format(ano))
else:
    print('O ano digitado não é Bissexto')
