lista = []

for c in range(0, 51):
    if c % 2 == 0:
        print('{} é um número par'.format(c))
        lista.append(c)
print(lista)
