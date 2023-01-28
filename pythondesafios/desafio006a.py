def dobro(n):
    return 2 * n

def triplo(n):
    return 3 * n

def raiz(n):
    return pow(n, 1/2)

def exibe():
    n = int(input('Digite um número inteiro: '))
    print('O dobro de n vale {}, o triplo vale {} e a raiz quadrada vale {}'.format(dobro(n), triplo(n), raiz(n)))

exibe()