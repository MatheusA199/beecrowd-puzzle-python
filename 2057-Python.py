entrada = input().split()

def escrever(frase):
	print(frase)

partida, chegada, fuso_horario = entrada
soma_total = int(partida) + int(chegada) + int(fuso_horario)


if (0 <= soma_total < 24):
	escrever(soma_total)

elif (soma_total < 0):
	escrever(24 + soma_total)

elif (soma_total > 24):
	escrever(soma_total - 24)