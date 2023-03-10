def fatorial(n=1, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    print('-' * 30)
    if show == True:
        c = n
        f = 1
        while c > 0:
            print(f'{c}', end='')
            print(' x ' if c > 1 else ' = ', end='')
            f *= c
            c -= 1
        print(f)
    else:
        f = 1
        for i in range(n, 0, -1):
            f *= i
        print(f)

fatorial(5, show=True)

'''while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    print()
    c -= 1'''
