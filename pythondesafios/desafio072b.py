lista = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
resp = ' '

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {lista[num]}')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp == 'N':
            break
    if num not in range(0, 21):
        print('Tente de novo...')










