def media(lar, com):

    print(f'A area de um terreno é {lar}x{com} é de {lar * com}m²')


print('Controle de Terrenos')
print('-'*20)
media(float(input('Largura: ')),
      float(input('Comprimento: ')))

