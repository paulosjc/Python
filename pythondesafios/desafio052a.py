n = int(input('Digite um número inteiro: '))

lista = []

for c in range(1, n + 1):
    if n % c == 0:
        lista.append(c)

if len(lista) == 2:
    print('O número {}, que foi digitado, é primo.'.format(n))
else:
    print('O número {} não é primo.'.format(n))
print(lista)