from datetime import date

lista = {'Ano': date.today().year}
dados = list
ano = (date.today().year)
lista["Nome"] = str(input('Nome: '))
nasci = int(input('Ano de Nascimento: '))
lista["ctps"] = int(input('Carteira de Trabalho (0 não tem): '))
lista["Ano"] = ano - nasci
if lista["ctps"] == 0:
    print('=-'*15)
    for v, l in lista.items():
        print(f'{v} tem o valor {l}.')
elif lista["ctps"] != 0:
    entrada = int(input('Ano de contratação: '))
    lista["contratação"] = (entrada + 35) - nasci
    lista["Salario"] = float(input('Salário: '))
    print('=-'*15)
    for v, l in lista.items():
        print(f'{v} tem o valor {l}.')
