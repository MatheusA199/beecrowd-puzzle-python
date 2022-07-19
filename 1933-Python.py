valor = input().split()
valor_int = []
for i in valor:
	valor_int.append(int(i))

a = max(valor_int)
print(a)