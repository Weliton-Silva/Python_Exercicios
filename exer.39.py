from datetime import date
nasc = int(input('Qual seu ano de nascimento ?'))
ano = date.today().year
alis = (ano - nasc)
if alis <= 10:
    print('Fique tranquilo falta alguns anos ainda para o alistamento')
elif alis == 11 and 12 and 13:
    print('Falta um pouco mais de meia década para alistamento')
elif alis == 14:
    print('Falta 4 anos para alistamento !')
elif alis == 15:
    print('Falta 3 Anos para alistamento !')
elif alis == 16:
    print('2 anos para alistamento !')
elif alis == 17:
    print('Apenas 1 Anos alistamento não esqueça !')
elif alis == 18:
    print('Chegou o seu ano de alistamento BOA SORTE !')
elif alis == 19:
    print('A sua fase de alismento foi ano passado !')
    print('Procure a sua junta militar mais proxima.')
elif alis == 20:
    print('Sua fase de alistamento passou a 2 anos.')
elif alis == 20:
    print('Procure algum orgão responsavel')
    print('seu prazo passou a 3 anos.')
else:
    print('Seu prazo de alistamento passou a {} anos'.format(alis - 18))




