lista = list()
nota1 = nota2 = 0
lista2 = list()
media = 0
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota2: '))
    lista.append(nome)
    lista.append(nota1)
    lista.append(nota2)
    cont = str(input('Deseja continuar ? [S/N]')).upper().split()[0]
    if cont == 'N':
        break
media = (nota1 + nota2) % 2
lista2.append(nome)
lista2.append(media)
print('=-'*30)
print('No. Nome        Média')
print('--'*30)
for n, m in enumerate(lista2):
    print(f'{n} {m}      {media}', )
print('=-'*30)
print(lista)
