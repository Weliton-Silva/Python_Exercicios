nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Média {}Aluno Reprovado'.format(media))
elif media <= 6.9:
    print('Média {}Aluno de Recuperação'.format(media))
else:
    print('Média {}Aluno Aprovado'.format(media))
