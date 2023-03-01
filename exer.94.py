dados = dict()
lista = list([[], []])
somaidade = 0
while True:
    nome = str(input('Nome: '))
    Sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    idade = int(input('Idade: '))
    somaidade = somaidade + idade
    if idade > somaidade / len(lista):
        dados["acimamedia"] = nome, Sexo, idade
    if Sexo == 'M':
        lista[0].append(nome)
        lista[0]. append(Sexo)
        lista[0].append(idade)
    if Sexo == 'F':
        lista[1].append(nome)
        dados["NomeF"] = nome
        lista[1].append(Sexo)
        lista[1].append(idade)
    cont = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
dados["MediaIdade"] = somaidade / len(lista)
print('-='*30)
print(f'O grupo tem {len(lista)} pessoas.')
print(f'A média de idade é de {dados["MediaIdade"]} anos.')
print(f'As mulheres cadastradas foram: {dados["NomeF"]}')
print(f'Lista de pessoas que estão acima da média:{dados["acimamedia"]}')

