pi = 3.14159

RAIO = float(input('Qual é o raio do círculo que você deseja que seja calculada a área, circunferência e diâmetro?\nINSIRA O RAIO AQUI: '))

ARE = pi * (RAIO **2)
CIRC = (2 * pi) * RAIO
DIA = 2 * RAIO

print(f'A área do círculo é igual a: {ARE}\nA circuferência do círculo é igual a: {CIRC}\nO diâmetro do círculo é igual a: {DIA}\n\fLEMBRETE: A UNIDADE DE MEDIDA É A MESMA QUE FOI ESCRITA.')
