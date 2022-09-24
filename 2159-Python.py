import math

def approximate_number_of_primes():
	n = entrada__num_natural()
	valor_minimo = calculo_valor_minimo(n)
	valor_minimo_round = arrendondar_valor(valor_minimo)

	valor_maximo = calculo_valor_maximo(valor_minimo)
	valor_maximo_round = arrendondar_valor(valor_maximo)

	escrever_valores(valor_maximo_round,valor_minimo_round)

def entrada__num_natural():
	n = int(input())
	return n 

def calculo_valor_minimo(n):
	valor_minimo = n / math.log(n)
	return valor_minimo

def calculo_valor_maximo(valor_minimo):
	valor_maximo = (valor_minimo * 1.25506)
	return valor_maximo
def arrendondar_valor(valor):
	arrendondado_valor = round(valor,1)
	return arrendondado_valor

def escrever_valores(valor_maximo_round,valor_minimo_round):
	print(f'{valor_minimo_round} {valor_maximo_round}')


if (__name__ == '__main__'):
	approximate_number_of_primes()