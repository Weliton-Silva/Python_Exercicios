from time import sleep

def maior(* num):
    print('-=' * 20)
    sleep(0.5)
    print('Analisando os valores passados...')
    sleep(0.5)
    for cont in num:
        print(cont, end=' ')
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor digitados foi {max(num)}.')
    sleep(0.5)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
