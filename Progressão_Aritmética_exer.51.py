n1 = int(input('Digite o termo que deseja saber a progressão aritmética: '))
razao = int(input('Digite a razão: '))
decimo = n1 + (10 - 1) * razao
for c in range(n1, decimo + razao, razao):
  print('{} '.format(c), end='..')
print('Fim da Progressão.')
