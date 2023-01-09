velo = float(input('Qual a Velocidade do automóvel ?'))
if velo > 80:
    print('Você Foi multado devido o excesso de velocidade !!')
    print('Multa de R$ {:.2f}'.format((velo - 80) * 7))
else:
    print('Você esta dentro do limite de velocidade prossiga com sua viagem !')
