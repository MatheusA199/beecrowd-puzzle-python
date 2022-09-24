pi = 3.14
while True:
	try:

		volume = float(input())
		diametro = float(input())

		area = ((diametro / 2)**2)*pi

		altura = volume / area

		print(f'ALTURA = {altura:0.2f}', end='\n')
		print(f'AREA = {area:0.2f}', end='\n')


	except EOFError:
 		break