def aumentar(preço=0, taxa=0, formato=False):
    """
    -> Calcula o aumento de um determinado preço, retornando o
    resultado com ou sem formatação.
    :param preço: o preço que se deseja reajustar.
    :param taxa: qual é a porcentagem do aumento.
    :param formato: quer a saída formatada ou não?
    :return: retorna o valor reajustado, com ou sem formatação.
    """
    res = preço * (1 + taxa / 100)
    return res if formato is False else moeda(preço)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço * (1 - taxa / 100)
    return res if not formato else moeda(preço)


def dobro(preço=0, formato=False):
    res = 2 * preço
    return res if formato is False else moeda(preço)

def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(preço)


def moeda(preço=0, moeda='R$'):
    return f'{moeda} {preço:>.2f} '.replace('.', ',')
