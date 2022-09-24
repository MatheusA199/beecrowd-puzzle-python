quantidade = int(input())

quantidade_mult2 = 0
quantidade_mult3 = 0
quantidade_mult4 = 0
quantidade_mult5 = 0

numeros = input().split()

for i in range(quantidade):
	if (int(numeros[i]) % 2 == 0):
		quantidade_mult2 +=1

	if (int(numeros[i]) % 3 == 0):
		quantidade_mult3 +=1

	if (int(numeros[i]) % 4 == 0):
		quantidade_mult4 +=1

	if (int(numeros[i]) % 5 == 0):
		quantidade_mult5 +=1

print(f'{quantidade_mult2} Multiplo(s) de 2')
print(f'{quantidade_mult3} Multiplo(s) de 3')
print(f'{quantidade_mult4} Multiplo(s) de 4')
print(f'{quantidade_mult5} Multiplo(s) de 5')