while True:
	X= int(input())
	line = []
	if X!=0:
		for i in range(1,(X+1)):
			line.append(i)
		print(*line)
	else:
		break