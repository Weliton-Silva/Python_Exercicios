n1 = int(input('Digite Primeiro Valor: '))
n2 = int(input('Digite o Segundo Valor: '))
if n1 > n2:
    print('O primeiro é valor maior {}\nO Segundo valor Digitado é {}'.format(n1, n2))
elif n2 > n1:
    print('O Segundo valor é o maior {}\nEm seguida o primeiro valor digitado é {}'.format(n2, n1))
else:
    print('Não existe valor maior.Os dois números são iguais.')
