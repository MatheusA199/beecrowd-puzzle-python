caso = 1

def escrever_sequencia():
			print(*lista_sequencia, end="\n")
			print("")

while True:
	try:
		lista_sequencia = [0]
		entrada= int(input())

		for i in range(1,entrada+1):
			for value in range(1, i+1):	
				lista_sequencia.append(i)

		tamanho_lista = len(lista_sequencia)
		verificacao = (tamanho_lista == 1)

		if (verificacao):	
			print(f"Caso {caso}: {tamanho_lista} numero")
			escrever_sequencia()
		else:
			print(f"Caso {caso}: {tamanho_lista} numeros")
			escrever_sequencia()

		caso += 1

	except EOFError:
		break
