dist = float(input('Quantos KM Deseja viajar ?'))
if dist <= 200:
    print('Você vai pagar R$ {:.2f}'.format(dist * 0.50))
else:
    print('Você vai pagar R$ {:.2f}'.format(dist * 0.45))
    



