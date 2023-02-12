num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
#num.pop(2)         Remove o elemento na posição 2
#num.remove(2)      Remove a primeira ocorrência do número 2 na lista
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5 na lista')
print(num)
print(f'Essa lista tem {len(num)} elementos')