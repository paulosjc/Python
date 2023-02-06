cont = 0
lista = []
n = 0
while n != 999:
    n = int(input('Digite um inteiro: '))
    if n != 999:
        cont += 1
        lista.append(n)

print('Foram digitados {} números'.format(cont))
print('A soma dos números digitados é {}'.format(sum(lista)))
