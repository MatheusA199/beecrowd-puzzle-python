#Número de entradas
tentativa = int(input())

#Ano atual
atual = 2015

for i in range(tentativa):
	data = int(input())
	ano_saida = (atual - data)

	maior = ano_saida > 0
	if (maior):
		print(f'{ano_saida} D.C.')

		#Tem que ser menos um, visto que não há ano zero.
	else:
		ano_saida -= 1
		print(f'{abs(ano_saida)} A.C.')

