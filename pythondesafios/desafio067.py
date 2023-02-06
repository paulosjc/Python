n = c = 0

while True:
    n = int(input('Qual tabuada você deseja? '))
    if n < 0:
        break
    for c in range(1, 11):
        mult = n * c
        print(f'{n} x {c} = {mult}')
