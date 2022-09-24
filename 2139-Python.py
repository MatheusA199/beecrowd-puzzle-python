def contagem_dias_natal():
	
	mes_quantidade_dias = {
	'1' : 31,
	'2': 29,
	'3' : 31,
	'4' : 30,
	'5' : 31,
	'6' : 30,
	'7' : 31,
	'8' : 31,
	'9' : 30,
	'10' : 31,
	'11' : 30,
	'12' : 25,
	}

	chaves = mes_quantidade_dias.keys()

	while True:
		try:
			dia, mes = entrada_dia_mes()

			dias = 0

			dezembro = (mes == 12)
			dia_natal = (dia == 25)
			vespera_natal = (dia == 24)
			passou_natal = (dia > 25)
			nao_antes_natal = (dia > 23)


			if (dezembro) and (nao_antes_natal):
			
				if (passou_natal):
					escrever_passou_dia_natal()
			
				elif (vespera_natal):
					escrever_vespera_natal()
			
				elif (dia_natal):
					escrever_dia_natal()

			else:
				for key in chaves:
					key_int = int(key)
					
					if (mes == key_int):
						dias = somar_dias_restantes(dias,mes,key,dia,mes_quantidade_dias)

					else:
						pass

				escrever_dias_restantes(dias)	

		except EOFError:
			break

def entrada_dia_mes():
	data = input().split()
	mes, dia = data
	dia = int(dia)
	mes = int(mes)
	return dia, mes

def escrever_dia_natal():
	print('E natal!')

def escrever_vespera_natal():
	print('E vespera de natal!')

def escrever_passou_dia_natal():
	print('Ja passou!')

def somar_dias_restantes(dias,mes,key,dia,mes_quantidade_dias):
	proximo_mes = (mes+1)
	dias += (mes_quantidade_dias[key] - dia)
	for value in range(proximo_mes,13):
		value = str(value)
		dias += mes_quantidade_dias[value]
	return dias

def escrever_dias_restantes(dias):
	print(f'Faltam {dias} dias para o natal!')

if (__name__ == '__main__'):
	contagem_dias_natal()