for c in range(0, 7, 2):
    print(c)
print('Fim.')

for c in range(7, 0, -1):
    print(c)
print('Fim.')

n = int(input('Digite um número: '))
for c in range(0, n + 1):
    print(c)

i = int(input('Digite o início: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))
for c in range(i, f + 1, p):
    print(c)
print('Fim.')

lista = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    lista.append(n)
print(lista)
print('Fim.')

s = 0
for c in range(0, 5):
    n = int(input('Digite um número: '))
    s += n
print(s)
print('Fim.')
