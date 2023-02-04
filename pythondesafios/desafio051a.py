lista = []
r = 3
pa = 0

for c in range(1, 101):
    pa = (c - 1) * r
    print(pa)
    lista.append(pa)

print(lista)
print('O primeiro termo é: {}'.format(lista[0]))
print('A razão dessa P.A. é {}'.format(lista[1] - lista[0]))
print('Os dez primeiros termos da P.A. são: {}'.format(lista[0:10]))