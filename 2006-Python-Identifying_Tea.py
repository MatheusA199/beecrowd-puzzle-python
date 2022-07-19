cha_preferido = int(input())

chas = input().split()

contador  = 0

for i in chas:
	verificacao = cha_preferido == int(i)

	if verificacao:
		contador += 1

	else:
		pass
print(contador) 