valor = float(input('valor do produto R$ '))
print('Digite [ 1 ]para pagamento à vista no dinheiro ou cheque')
print('Digite [ 2 ] para pagamento a vista no cartão')
print('Digite [ 3 ] para pagamento no cartão em até 2x')
print('Digite [ 4 ] para pagamento cartão 3x ou mais')
print('Digite [ 0 ] para cancelar')
paga =int(input('Digite a Forma de pagamento: '))
juros = (20 * valor) /100 + valor
if paga == 1:
    print('O valor a ser pago à vista com 10% de desconto é {:.2f}'.format((10 * valor) /100 - valor))
elif paga == 2:
    print('O valor a ser pago à vista com 5% de desconto é {:.2f}'.format((5 * valor) /100 - valor))
elif paga == 3:
    print('O valor parcelado em 2x fica {:.2F}'.format(valor / 2))
elif paga == 4:
    print('para pagamento parcelado em mais de 3x fica {:.2f}\n3x de {:.2f}\nOu 4x {:.2f}'.format(juros, juros / 3, juros / 4))
elif paga == 0:
    print('Operação cancelada')
else:
    print('Digito incorreto tente novamente')




