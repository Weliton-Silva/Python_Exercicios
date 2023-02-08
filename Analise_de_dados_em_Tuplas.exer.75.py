n1 = (int(input('Digite um número: ')),
      int(input('Digite outro número: ')),
      int(input('Digite mais um número: ')),
      int(input('Digite o último número: ')))
print('=-'*20)
print(f'Você Digitou {n1}')
print(f'O número 9 aparece {n1.count(9)} vezes.')
if 3 in n1:
    print(f'O número 3 foi digitado a primeira vez {n1.index(3) + 1}º posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram', end=' ')
for cont in n1:
    if cont % 2 == 0:
        print(cont, end=' ')
