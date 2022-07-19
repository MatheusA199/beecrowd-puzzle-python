while True:
	try:
		horarios = []
		diferencas = []
		tempo = 0
		hora = input().split(":")
		horarios.append(int(hora[0]) + float(hora[1])/60)

		for i in range(len(horarios)):
			diferencas.append(8 - horarios[i])

		for i in range(len(horarios)):
			diferenca = ((diferencas[i] - 1)*60)
			verificacao = (diferenca) < 0

			if (verificacao):
				tempo =  diferenca
				tempo_ajustado = abs(round(tempo))
				print(f"Atraso maximo: {tempo_ajustado}")
			else:
				print(f"Atraso maximo: 0")

	except EOFError:
		break