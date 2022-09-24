def two_bills():
	while True:
		valores_possiveis = [4, 7, 10, 12, 15, 20, 22, 25, 30, 40, 52, 55, 60, 70, 100, 102, 105, 110, 120, 150, 200]

		total, valor_pago = entrada_valores()

		if (total == 0) and (valor_pago == 0):
			break

		troco = calcular_troco(valor_pago, total)
		possivel = verificar_se_possivel(valores_possiveis,troco)
		print(possivel)

		if (possivel == True):
			escrever_possible()

		else:
			escrever_impossible()


def entrada_valores():
	entradas = input().split()
	total, valor_pago = entradas

	total = int(total)
	valor_pago = int(valor_pago)

	return total,valor_pago

def calcular_troco(valor_pago, total):
	troco = abs(valor_pago - total)
	return troco

def escrever_possible():
	print('possible')

def escrever_impossible():
	print('impossible')

def verificar_se_possivel(valores_possiveis,troco):
	for value in valores_possiveis:
		if (troco == value):
			return True


if (__name__ == '__main__'):
	two_bills()