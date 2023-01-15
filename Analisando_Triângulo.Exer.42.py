r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Formara um triângulo')
    if r1 == r2 == r3:
        print('Equilatero !')
    elif r1 != r2 != r3 != r1:
        print('Escaleno !')
    else:
        print('Isóceles')
else:
    print('Não formara um triângulo')