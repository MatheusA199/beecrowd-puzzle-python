def password():	
	while True:
		try:
			numero = entrada_numero()
			escrever_senha(numero)
		except:
			break

def entrada_numero():
	numero = int(input())
	return numero
	
def escrever_senha(numero):
	senha = (numero-1)
	print(senha)

if (__name__ == '__main__'):
	password()