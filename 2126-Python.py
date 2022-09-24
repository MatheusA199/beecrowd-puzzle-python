caso = 0
while True:
	try:

		caso +=1
		contador = 0
		posicao = 0
		numero1 = input()
		numero2 = input()
		tamanho1 = len(str(numero1))
		tamanho2 = len(str(numero2))

		for i in range(0,tamanho2):
			if (numero2[i:i+tamanho1] == str(numero1)):
				contador += 1
				posicao = i + 1

			else:
				pass

		print(f'Caso #{caso}:', end='\n')

		if (contador != 0):
			print(f'Qtd.Subsequencias: {contador}', end='\n')
			print(f'Pos: {posicao}', end='\n')
			
		else:
			print('Nao existe subsequencia', end='\n')

		print('')

	except EOFError:
		break