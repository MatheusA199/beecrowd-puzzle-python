def name_at_form():
	nome = entrada_nome()
	tamanho = calculo_tamanho_nome(nome)
	criterio_menor = (tamanho <=80)

	if (criterio_menor):
		print('YES')
	else:
		print('NO')

def entrada_nome():
	nome = str(input())
	return nome

def calculo_tamanho_nome(nome):
	tamanho = len(nome)
	return tamanho
	
if (__name__ == '__main__'):
	name_at_form()