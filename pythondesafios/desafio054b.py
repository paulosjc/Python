from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1, 8):
    nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(pessoa)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print('São {} pessoas maiores de idade'.format(totmaior))
print('São {} pessoas menores de idade'.format(totmenor))
