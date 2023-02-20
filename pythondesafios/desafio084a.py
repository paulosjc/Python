dados = list()
lista = list()
cont = 0
pesados = list()
leves = list()

while True:
    nome = str(input('Entre com o nome: '))
    peso = int(input('Entre com o peso: '))
    dados.append(nome)
    dados.append(peso)
    if peso >= 100:
        pesados.append(nome)
        pesados.append(peso)
    elif peso <= 70:
        leves.append(nome)
        leves.append(peso)
    lista.append(dados[:])
    cont += 1
    dados.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break


print(f'Foram cadastradas {cont} pessoas')
print(f'Os mais pesados são {pesados}')
print(f'Os mais leves são {leves}')