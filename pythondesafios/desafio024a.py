cidade = str(input('Digite o nome da cidade: ')).upper().strip()
print('SANTO' in cidade)
cidade2 = cidade.split()
print(cidade2)
if cidade2[0] == 'SANTO':
    print('O nome da cidade começa com SANTO')
else:
    print('O nome da cidade não começa com SANTO')

