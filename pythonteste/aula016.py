'''lanche = ('hambúrguer', 'suco', 'pizza', 'pudim', 'batata frita')

for c in lanche:
    print(c)

for i in range(0, 11):
    print(i)

print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2])
print(lanche[-3:])

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche))'''

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(c)
print(d)
print(d.count(9))
print(c.index(8))
print(d.index(5, 1))

pessoa = ('Paulo', 43, 'M', 80)
print(pessoa)