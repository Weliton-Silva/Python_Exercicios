dados = dict()
lista = []

dados["Nome"] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dados["Nome"] } jogou ? '))
for p in range(partidas):
    lista.append(int(input(f'Quantos gols na partida {p +1} ? ')))
dados["Jogos"] = lista
dados["Total"] = sum(lista)
print('-='*20)
print(f'{dados}, {lista},')
print('-='*20)
for d, v in dados.items():
    print(f'O campo {d} tem o valor {v}')
print('-='*20)
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas.')
for l, g in enumerate(lista):
    print(f'   => Na partida {l+1}º, fez {g} gols.')
print(f'Foi um total de {dados["Total"]} gols.')
