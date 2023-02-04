lista = []
s = 0
cont = 0

for c in range(1, 7):
    n = int(input('Digite o {}º valor: '.format(c)))
    if n % 2 == 0:
        s += n
        cont += 1
        lista.append(n)

if len(lista) == 1:
    print('A soma do número par {} digitado é: {}'.format(lista[0], s))
elif len(lista) == 0:
    print('Você não digitou nenhum número par')
else:
    print('A soma dos {} números pares digitados é: {}'.format(cont, s))
print(lista)