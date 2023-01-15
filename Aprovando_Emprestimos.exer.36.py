casa = float(input('Qual o valor do imóvel ? R$'))
salario = float(input('Qual seu salario ? R$'))
anos = int(input('Quantos anos deseja pagar ? '))
parce = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação vai ser de R${:.2f}'.format(casa, anos, parce))
if parce <= minimo:
    print('Parabens ! Seu financiamento foi aprovado.')
    print('Parcelas de {:.2f}'.format(parce))
else:
    print('Seu empréstimo foi negado.')
