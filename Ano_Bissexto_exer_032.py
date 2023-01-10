from datetime import date
ano = int(input('Digite o Ano desejado ou coloque 0 para analisar o ano atual:  '))
if ano == 0:
    ano = date.today().year
    print('o ano autal {}'.format(ano))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano Bissexto'.format(ano))
else:
    print('O ano digitado não é Bissexto')
