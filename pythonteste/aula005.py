nome = 'Paulo'
idade = 43

print('O nome dele é %s e tem %d anos.' % (nome, idade))
print('O nome dele é {} e tem {} anos.'.format(nome, idade))
print(f'O nome dele é {nome} e tem {idade} anos.')


while True:
    n = int(input('Digite um número: '))
    if n not in range(0, 11):
        print('Reposta inválida. Digite de novo...')

while True:
    n = int(input('Digite um número: '))
    if 0 <= n <= 10:
        break
    print('Reposta inválida. Digite de novo...')

while True:
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))

números = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')

    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
print('=-' * 30)
números.sort()
print(f'Você digitou os valores {números}')
print('=-' * 30)

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}.')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram: {lista}')
print('-=' * 30)
