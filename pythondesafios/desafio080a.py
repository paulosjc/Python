lista = []
maior = menor = 0

for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if i == 0:
        maior = menor = n
        lista.append(n)
    else:
        menor = min(lista)
        maior = max(lista)
        if n > maior:
            lista.append(n)
        if n < menor:
            lista.insert(0, n)

print(lista)
