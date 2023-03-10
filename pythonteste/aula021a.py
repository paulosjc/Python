# Interactive Help e DocStrings

help()
help(print)
print(print.__doc__)
help(input)
print(input.__doc__)

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada pelo Gustavo Guanabara do canal Curso em Vídeo.
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

contador(2, 10, 2)

help(contador)

