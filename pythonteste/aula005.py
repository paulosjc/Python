'''nome = 'Paulo'
idade = 43

print('O nome dele é %s e tem %d anos.' % (nome, idade))
print('O nome dele é {} e tem {} anos.'.format(nome, idade))
print(f'O nome dele é {nome} e tem {idade} anos.')'''

'''n = 12
while True:
    n = int(input('Digite um número: '))
    if n not in range(0, 11):
        print('Reposta inválida. Digite de novo...')'''

while True:
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
