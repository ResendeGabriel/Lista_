num = int(input('Digite um número inteiro de CINCO dígitos: '))

n1p = round(num/10000)
n2p = round(num/1000)
n3p = round(num/100)
n4p = round(num/10)
n5p = round(num/1)

###################################################################

n1 = n1p
n2 = -1*(n1p * 10) + n2p
n3 = -1*(n2p * 10) + n3p
n4 = -1*(n3p * 10) + n4p
n5 = -1*(n4p * 10) + n5p


print(f'Seu número: {n1}   {n2}   {n3}   {n4}   {n5}')
