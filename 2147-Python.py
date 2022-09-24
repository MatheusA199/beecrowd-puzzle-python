def galopeira():
	teste = int(input())

	for i in range(teste):
		palavra = entrada_palavra()

		tamanho = calcular_tamanho_galopeira(palavra)
		tamanho_certo = tamanho / 100

		print(f'{tamanho_certo:.2f}')

def entrada_palavra():
	palavra = str(input())
	return palavra

def calcular_tamanho_galopeira(palavra):
	tamanho = len(palavra)
	return tamanho

def tamanho_certo(tamanho):
	tamanho_certo = (tamanho / 100)
	return tamanho_certo

def escrever_galopeira(tamanho_certo):
	print(f'{tamanho_certo:.2f}')

if (__name__ == '__main__'):
	galopeira()