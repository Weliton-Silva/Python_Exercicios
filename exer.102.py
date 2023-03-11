def fatorial(n, show=False):
    """-> Calcula Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do Fatorial de um número n."""
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=False))
