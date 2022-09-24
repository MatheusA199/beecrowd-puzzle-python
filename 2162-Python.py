def peaks_and_valleys():
	termos = entrada_casos()

	casos = entrada_alturas()

	dois_termos_iguais = (termos == 2) and (casos[0] == casos[1])

	if (dois_termos_iguais):
		situacao = 0

	else:
		situacao = 1
		for i in range(1, termos-1):
			vale_pico_vale = (casos[i-1] < casos[i] > casos[i+1])
			pico_vale_pico = (casos[i-1] > casos[i] < casos[i+1])

			if not((vale_pico_vale) or (pico_vale_pico)):
				situacao = 0
				break

	escrever_saida(situacao)

def entrada_casos():
	termos = int(input())
	return termos

def entrada_alturas():
	casos = list(map(int, input().split()))
	return casos

def escrever_saida(situacao):
	print(situacao)

if (__name__ == '__main__'):
	peaks_and_valleys()