n1 = int(input('Com Qual Tabuada gostaria de inciar ? '))
cont = 1
while True:
    print(f'{n1} x {cont:2} = {n1*cont}')
    cont += 1
    if cont == 11:
        print('-'*30)
        n1 = int(input('Quer ver a tabuada de qual valor ? '))
        cont = 1
    if n1 < 0:
        break
print('-'*30)
print('Fim da Tabuada')
