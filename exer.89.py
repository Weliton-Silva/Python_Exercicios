lista = []
nota1 = nota2 = media = 0
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    cont = str(input('Deseja continuar ? [S/N]')).upper().split()[0]
    if cont == 'N':
        break
print('=-'*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar a nota de qual aluno ? (999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(lista)-1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
    print('FIM DO PROGRAMA')
