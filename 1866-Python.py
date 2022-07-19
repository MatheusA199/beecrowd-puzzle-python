n = int(input())
for i in range(n):
	valor = int(input())

	positivo = (valor% 2 == 0)

	if (positivo):
		print(0)
	else:
		print(1)