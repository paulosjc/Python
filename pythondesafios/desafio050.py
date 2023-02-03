lista = []
s = 0

for c in range(0, 6):
    n = int(input('Entre com um número qualquer: '))
    if n % 2 == 0:
        s += n
        lista.append(n)

print('A soma dos números pares digitados é: {}'.format(s))
print(lista)