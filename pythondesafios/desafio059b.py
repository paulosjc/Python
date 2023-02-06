from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0

while opção != 5:
    print('Qual é a sua opção? ')
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
    opção = int(input('=> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma {} + {} vale {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('A multiplicação {} x {} vale {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
            print('O maior valor entre {} e {} é {}'.format(n1, n2, maior))
        elif n1 < n2:
            maior = n2
            print('O maior valor entre {} e {} é {}'.format(n1, n2, maior))
        else:
            print('Os números são iguais.')
    elif opção == 4:
        print('Digite novos números: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente de novo.')
    print('-=-' * 10)
    sleep(2)
print('Fim do programa.')
