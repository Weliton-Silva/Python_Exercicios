sal = float(input('Qual salario do Funcionario ?'))
novo_sal = (10 * sal) / 100 + sal
novo_sal2 = (15 * sal) / 100 + sal
if sal >= 1250:
    print('Novo salario do funcionario é R$ {:.2f}'.format(novo_sal))
if sal < 1250:
    print('Salario atualizado é R$ {:.2f}'.format(novo_sal2))
