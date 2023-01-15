peso = int(input('Digite o seu peso (Kg): '))
alt = float(input('Digite sua altura (M): '))
imc = (peso / alt ** 2)
if imc < 18.5:
    print('IMC: {:.2f}'.format(imc))
    print('Você está Abaixo do Peso.')
elif imc <= 25:
    print('IMC: {:.2f}.'.format(imc))
    print('Você está com Peso Ideal.')
elif imc <= 30:
    print('IMC: {:.2f}'.format(imc))
    print('Você esta com Sobrepeso')
elif imc <= 40:
    print('IMC: {:.2f}'.format(imc))
    print('Você esta com Obesidade')
else:
    print('IMC: {:.2f}'.format(imc))
    print('Você esta com Obesidade Mórbida')
