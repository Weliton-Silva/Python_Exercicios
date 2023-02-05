num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
n1 = int(input('Digite um número entre 0 e 20: '))
while n1 < 0 or n1 > 20:
    n1 = int(input('Tente Novamente. Digite um número entre 0 e 20: '))
for cont in range(n1, len(num)):
    print(f'Você digitou o número {num[n1]}')
    break