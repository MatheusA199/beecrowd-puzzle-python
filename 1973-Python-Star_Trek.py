#Série de inputs para saber quantas fazendas são, o número de carneiros
farm = input()
ovelhas = [int(i) for i in input().split()]
total_original = sum(ovelhas)

#Lista e o total de ovelhas
lista_original = ovelhas.copy()

#Ter uma copiar da lista original, o número da fazenda a ser atacada; o tamanho da lista; e quantas ovelhas sobraram
numero_fazenda = 0
tamanho = len(ovelhas) - 1
total_final = 0

#funções
def roubar_ovelha():
	ovelhas[numero_fazenda] = ovelhas[numero_fazenda] - 1

def somar_valor():
	global total_final
	total_final += ovelhas[numero_fazenda]

def ovelhas_impar():
	global numero_fazenda
	numero_fazenda += 1

def ovelhas_par():
	global numero_fazenda
	numero_fazenda -=1

while (tamanho >= numero_fazenda >= 0):
	if (ovelhas[numero_fazenda] != 0):
		if (ovelhas[numero_fazenda]%2 != 0):
			roubar_ovelha()
			somar_valor()
			ovelhas_impar()
		elif (ovelhas[numero_fazenda]%2 == 0):
			roubar_ovelha()
			somar_valor()
			ovelhas_par()
	else:
		break

resto_ovelhas = (total_original - abs(total_original - total_final))
fazendas_atacadas = 0

for i in range(tamanho+1):
	if (lista_original[i] != ovelhas[i]):
		fazendas_atacadas += 1
	else:
		pass
print(f'{fazendas_atacadas} {resto_ovelhas}')
