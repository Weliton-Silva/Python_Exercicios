import moedas

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {moedas.metade(p)}')
print(f'O dobro de {p} é {moedas.dobro(p)}')
print(f'Aumentando 10%, temos R${moedas.aumentar(p, 10)}')
print(f'Aumentando 13%, temos R${moedas.diminuir(p, 13)}')
