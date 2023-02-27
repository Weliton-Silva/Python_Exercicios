from datetime import date

lista = {'Ano': date.today().year}
dados = list
ano = (date.today().year)
lista["Nome"] = str(input('Nome: '))
lista["Ano"] = int(input('Ano de Nascimento: '))
lista["ctps"] = int(input('Carteira de Trabalho (0 não tem): '))

if lista["ctps"] == 0:
    print('=-'*15)
    for v, l in lista.items():
        print(f'{v} tem o valor {l}.')
        if l > 10:
elif lista["ctps"] != 0:
    lista["Salario"] = int(input('Salário: '))
