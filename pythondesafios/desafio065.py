resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
média = soma / quant
print('Você digitou {} números e a média é {}'.format(quant, média))
print('O maior valor é {} e o menor valor é {}'.format(maior, menor))
