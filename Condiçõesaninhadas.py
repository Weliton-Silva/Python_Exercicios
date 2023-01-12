valor = float(input('Qual 0 valor da Casa ? '))
sal = float(input('Qual seu salario ? '))
parc = int(input('Quantas parcelas deseja simular ? '))
desc = (30 * sal) / 100
prest = (valor / parc)
if sal > prest + desc:
    print('Você pagará {:.2f} de prestação'.format(prest))
else:
    print('seu emprestimo não foi aceito pelo banco')
