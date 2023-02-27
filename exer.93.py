dados = dict()
lista = []
dados["Nome"] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dados["Nome"] } jogou ? '))
for p in range(partidas):
    lista.append(int(input(f'Quantos gols na partida {p +1} ? ')))
