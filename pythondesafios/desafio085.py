lista = list()
pares = list()
ímpares = list()

for i in range(0, 7):
    valor = int(input(f'Digite o {i + 1}º valor: '))
    if valor % 2 == 0:
        pares.append(valor)
    if valor % 2 == 1:
        ímpares.append(valor)

lista.append(pares[:])
lista.append(ímpares[:])
print(lista)
print(sorted(lista[0]))
print(sorted(lista[1]))
