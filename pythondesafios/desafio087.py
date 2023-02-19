lista = []
lista1 = []
lista2 = []
lista3 = []
pares = []
coluna3 = []
linha2 = []
cont = 0
c = 0
v = 0

while cont < 3:
    valor = int(input('Entre com um valor: '))
    cont += 1
    lista1.append(valor)
    while 3 <= cont <= 5:
        valor = int(input('Entre com um valor: '))
        cont += 1
        lista2.append(valor)
        while 6 <= cont <= 8:
            valor = int(input('Entre com um valor: '))
            cont += 1
            lista3.append(valor)
            if cont == 9:
                break

lista.append(lista1)
lista.append(lista2)
lista.append(lista3)
print(lista)
print(lista1)
print(lista2)
print(lista3)
print(f'{[lista[0][0]]}', end='')
print(f'{[lista[0][1]]}', end='')
print(f'{[lista[0][2]]}')
print(f'{[lista[1][0]]}', end='')
print(f'{[lista[1][1]]}', end='')
print(f'{[lista[1][2]]}')
print(f'{[lista[2][0]]}', end='')
print(f'{[lista[2][1]]}', end='')
print(f'{[lista[2][2]]}')

for i in range(0, 3):
    for c in lista[i][:]:
        if c % 2 == 0:
            pares.append(c)

print(f'A soma dos valores pares é: {sum(pares)}')

coluna3.append(lista[0][2])
coluna3.append(lista[1][2])
coluna3.append(lista[2][2])

print(f'A soma dos valores da terceira coluna é: {sum(coluna3)}')

linha2.append(lista[1][0])
linha2.append(lista[1][1])
linha2.append(lista[1][2])

print(f'A soma dos valores da segunda linha é: {sum(linha2)}')
