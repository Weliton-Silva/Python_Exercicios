try:
    a = int(input('Númerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Tivemos problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuario preferiu não informar dados !')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado {r:.1f}')
finally:
    print('Volte sempre ! Muito Obrigado.')
