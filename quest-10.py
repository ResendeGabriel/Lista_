a = int(input('Digite um número: '))
b = int(input('Digite mais outro número: '))
c = int(input('Digite mais uma vez outro número: '))
d = int(input('Digite outro número (juro que essa foi a última vez): '))

if a >= b and a >= c and a >= d:
    mai = a

elif b >= a and b >= c and b >= d:
    mai = b

elif c >= a and c >= b and c >= d:
    mai = c

elif d >= a and d >= b and d >= c:
    mai = d


if a <= b and a <= c and a <= d:
    men = a

elif b <= a and b <= c and b <= d:
    men = b

elif c <= a and c <= b and c <= d:
    men = c

elif d <= a and d <= b and d <= c:
    men = d

if a == b == c == d:
    print('Todos os números são iguais!')

else:
    print(f'O maior número desses é: {mai} e o menor é: {men}.')