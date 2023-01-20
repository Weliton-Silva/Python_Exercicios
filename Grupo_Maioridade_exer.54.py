from datetime import date
ano = date.today().year
cont = 0
for c in range(1, 8):
    nasc = int(input('Digite o Ano de Nascimento: '))
if ano - nasc >= 21:
    cont += 1
    restante = 7 - cont
print('Os que atingiram a maior idade são {}'.format(cont))
print('Os que nao atingiram maior idade são {}'.format(restante))

