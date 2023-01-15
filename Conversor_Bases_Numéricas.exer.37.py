valor = int(input('Digite Qual valor inteiro: '))
print('Escolha a forma de conversão')
print('Digite [ 1 ] Binário.')
print('Digite [ 2 ] Octal.')
print('Digite [ 3 ] hexadecimal.')
base = int(input('Digite a opção desejada: '))
if base == 1:
    print('Binário do valor digitado é {}'.format(bin(valor)[2:]))
elif base == 2:
    print('Conversão do valor digitado em Octal é {}'.format(oct(valor)[2:]))
elif base == 3:
    print('Conversão do valor digitado em Hexadecimal é {}'.format(hex(valor)[2:]))
else:
    print('Número Invalido')
