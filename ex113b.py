def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print(f'\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print(f'\n\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print(f'\033[0;31mERRO: por favor digite um valor Real Válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print(f'\n\033[0;31mEntrada de dados interrompida pelo usuario.\033[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um número inteiro : ')
n2 = leiaFloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {n1} e o valor real foi {n2}')
