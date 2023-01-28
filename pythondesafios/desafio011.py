w = float(input('Entre com a largura em metros: '))
h = float(input('Entre com a altura em metros: '))
a = w * h
q_tinta = a / 2
print('Sua parede tem dimensões de {:.2f} m x {:.2f} m e uma área de {:.2f} m²'.format(w, h, a))
print('A quantidade de tinta necessária para pintar {:.2f} m² é de {:.2f} l.'.format(a, q_tinta))
print(f'São necessários {q_tinta} l de tinta para pintar {a} m² de área.')