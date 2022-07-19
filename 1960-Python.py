#Para passar para int
p = input().split()
p_int = []
for i in p:
	p_int.append(int(i))

#Para passar as height para int
n_int = []
n = input().split()
for i in n:
	n_int.append(int(i))

salto = p_int[0]
vezes = p_int[1]
verificacao = 1
for value in range(1,vezes):
	possivel = (abs(n_int[value] - n_int[value-1]) <= salto)

	if (possivel):
		verificacao +=1
	else:
		print('GAME OVER')
		break

if (verificacao == vezes):
	print('YOU WIN')


