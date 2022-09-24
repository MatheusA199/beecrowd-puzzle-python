def pepe_i_already_took_the_candle():
	casos = int(input())

	for i in range(casos):
		hora,minuto,situacao_porta = entrada_dados()

		porta_aberta = (situacao_porta == 1)

		if (porta_aberta):
			escrever_abriu(hora, minuto)
		else:
			escrever_fechou(hora, minuto)

def entrada_dados():
	entradas = list(map(int, input().split()))
	return entradas

def escrever_abriu(hora, minuto):
	print(f'{hora:02.0f}:{minuto:02.0f} - A porta abriu!')

def escrever_fechou(hora, minuto):
	print(f'{hora:02.0f}:{minuto:02.0f} - A porta fechou!')

if (__name__ == '__main__'):
	pepe_i_already_took_the_candle()