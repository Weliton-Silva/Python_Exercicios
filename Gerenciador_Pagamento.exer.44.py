valor = float(input('valor do produto R$ '))
print('Digite [ 1 ]para pagamento à vista no dinheiro ou cheque')
print('Digite [ 2 ] para pagamento a vista no cartão')
print('Digite [ 3 ] para pagamento no cartão em até 2x')
print('Digite [ 4 ] para pagamento cartão 3x ou mais')
print('Digite [ 0 ] para cancelar')
paga =float(input('Digite a Forma de pagamento: '))
juros = (20 * valor) /100 + valor
if paga == 1:
    print('O valor a ser pago à vista com 10% de desconto é R${:.2f}'.format(valor - (10 * valor / 100)))
elif paga == 2:
    print('O valor a ser pago à vista com 5% de desconto é R${:.2f}'.format(valor - (5 * valor / 100)))
elif paga == 3:
    print('O valor parcelado em 2x é de R${:.2f}'.format(valor / 2))
elif paga == 4:
    parc = int(input('Quantas parcelas ?'))
    print('Pagamento parcelado {}x de R$ {:.2f} com Juros'.format(parc, juros / parc))
    print('Sua compra de R${:.2f} Vai custar R${:.2f} No final'.format(valor, juros))
elif paga == 0:
    print('Operação cancelada')
else:
    print('Digito incorreto tente novamente')
