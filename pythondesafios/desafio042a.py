print('\033[32m-=-\033[m' * 10)
print('\033[33mAnalisador de Triângulos\033[m')
print('\033[32m-=-\033[m' * 10)

r1 = float(input('Primeiro lado: '))
r2 = float(input('Segundo lado: '))
r3 = float(input('Terceiro lado: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[33mCom estes segmentos É possível formar um triângulo.')
    if r1 == r2 == r3:
        print('Este triângulo é \033[33mEQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
        print('Este triângulo é \033[32mESCALENO.')
    else:
        print('Este triângulo é \033[34mISÓSCELES.')
else:
    print('\033[31mCom estas medidas NÃO é possível formar um triângulo.')
