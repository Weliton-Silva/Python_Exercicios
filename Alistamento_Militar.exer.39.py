from datetime import date
nasc = int(input('Qual seu ano de nascimento ?'))
ano = date.today().year
alis = (ano - nasc)
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, alis, ano))
if alis == 18:
    print('Você tem que se alistar imediatamente !')
elif alis < 18:
    saldo = 18 - alis
    print('Você não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
    print('Seu alistamento será {}'.format(saldo + ano))
elif alis > 18:
    saldo = alis - 18
    print('Você ja deveria ter se alistamento há {} anos.'.format(saldo))
    print('Seu Alistamento foi em {}'.format(ano - saldo))