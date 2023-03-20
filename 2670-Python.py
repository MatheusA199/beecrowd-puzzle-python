class MaquinaDeCafe:
	def __init__(self):		
		self._qtn_andares = 3
		self._qtn_list_level = self.recebe_retorna_lista()

	@staticmethod
	def recebe_entrada():
		entrada = input()
		return entrada

	def recebe_input_transforma_int(self):
		entrada = self.recebe_entrada()
		numero = int(entrada)
		return numero

	def recebe_retorna_lista(self):
		lista = []
		for i in range(self._qtn_andares):
			numero_pessoas_do_andar = self.recebe_input_transforma_int()
			lista.append(numero_pessoas_do_andar)

		return lista

	def calcula_qtn_minutos(self):
		first_qtn_min = self._qtn_list_level[1] * 2 + self._qtn_list_level[2] * 4
		second_qtn_min = self._qtn_list_level[0] * 2 + self._qtn_list_level[2] * 2
		third_qtn_min = self._qtn_list_level[0] * 4 + self._qtn_list_level[1] * 2

		list_qtn_minutos = [first_qtn_min, second_qtn_min, third_qtn_min]

		return min(list_qtn_minutos)
		

	def __str__(self):
		qtn_minutos_total = str(self.calcula_qtn_minutos())
		return qtn_minutos_total

def maquina_de_cafe():
	objeto_maquina_de_cafe = MaquinaDeCafe()
	print(objeto_maquina_de_cafe)

if __name__ == '__main__':
	maquina_de_cafe()




