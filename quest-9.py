a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))

if a > b:
    print(f'O maior número entre esses dois é {a}, já o menor é {b}.')

elif a < b:
    print(f'O maior número entre esses dois é {b}, já o menor é {a}.')

else:
    print(f'Os números {a} e {b} são iguais!')
