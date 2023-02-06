n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

print('\033[33m-=-' * 15)
print('\033[34m     Qual operação você deseja efetuar?\033[m')
print('\033[33m-=-\033[m' * 15)
print('[1] Somar')
print('[2] Multiplicar')
print('[3] Maior')
print('[4] Novos números')
print('[5] Sair do programa')
op = 1

while op == 1 or op == 2 or op == 3 or op == 4:
    op = int(input('Digite sua opção: '))
    if op == 1:
        r = n1 + n2
        print('A soma vale {}'.format(r))
    elif op == 2:
        r = n1 * n2
        print('A multiplicação vale {}'.format(r))
    elif op == 3:
        if n1 > n2:
            maior = n1
            print('O maior valor é {}'.format(n1))
        elif n1 < n2:
            maior = n2
            print('O maior valor é {}'.format(n2))
        else:
            print('Os números são iguais.')
    elif op == 4:
        print('Digite novos números: ')
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
    elif op == 5:
        exit()



