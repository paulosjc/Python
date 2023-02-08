lista = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n = ' '
while n not in range(0, 21):
    n = int(input('Digite um número entre 0 e 20: '))
    if n not in range(0, 21):
        print('Opção inválida. Digite novamente...')
    if n in range(0, 21):
        print(f'Você digitou {lista[n]}')