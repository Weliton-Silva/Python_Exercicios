from random import randint

n1 = randint(0, 10)
n2 = randint(0, 10)
n3 = randint(0, 10)
n4 = randint(0, 10)
n5 = randint(0, 10)
valores = (n1, n2, n3, n4, n5)
menor = 0
maior = 0
print(f'Os valores sorteados foram: {valores}')
print(f'O menor valor sorteado foi: {sorted(valores)[0]}')
print(f'O maior valor sorteado foi: {sorted(valores)[-1]}')
