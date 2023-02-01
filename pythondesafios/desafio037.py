n = int(input('Digite um número inteiro qualquer: '))
print('''Digite uma das opções de conversão:
[ 1 ] Converte para binário
[ 2 ] Converte para octal
[ 3 ] Converte para hexadecimal''')
base = int(input('Digite sua opção: '))
if base == 1:
    n_2 = bin(n)
    print('O número {} em binário é {}'.format(n, n_2[2:]))
elif base == 2:
    n_8 = oct(n)
    print('O número {} em octal é {}'.format(n, n_8[2:]))
elif base == 3:
    n_16 = hex(n)
    print('O número {} em hexadecimal é {}'.format(n, n_16[2:]))
else:
    print('Opção inválida!')