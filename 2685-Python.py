class TheChange:
	def __init__(self):
		self._angle = self.recebe_input_transforma_int()

	def verifica_periodo_dia(self):
		if 0 <= self._angle < 90 or self._angle == 360:
			return 'Bom Dia!!'

		elif 90 <= self._angle < 180:
			return 'Boa Tarde!!'

		elif 180 <= self._angle < 270:
			return 'Boa Noite!!'

		else:
			return 'De Madrugada!!'

	def __str__(self):
		return self.verifica_periodo_dia()

	@staticmethod
	def recebe_entrada():
		entrada = input()
		return entrada

	def recebe_input_transforma_int(self):
		entrada = self.recebe_entrada()
		numero = int(entrada)
		return numero


def the_change():
	while True:
		try:
			objeto_the_change = TheChange()
			print(objeto_the_change)

		except EOFError:
			break


if __name__ == '__main__':
	the_change()