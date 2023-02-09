palavras = ('Aprender', 'Programas', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado',' Programador', 'Futuro')
for cont in palavras:
    print(f'\nNa Palavra {cont} temos ', end=' ')
    for letra in cont:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
