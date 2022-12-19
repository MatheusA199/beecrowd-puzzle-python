class BuscadorDePaoDeQueijo:
	def __init__(self):
		self._linhas, self._colunas = self.recebe_lista()
		self.matrix = self.recebe_matrix()

	@staticmethod
	def recebe_numero():
		numero = int(input())
		return numero

	@staticmethod
	def recebe_lista():
		lts = list(map(int, input().split(' ')))
		return lts

	def recebe_matrix(self):
		lts = []
		for i in range(self._linhas):
			linha = self.recebe_lista()
			lts.append(linha)

		return lts

	def calcula_numero_chesse_bread(self):
		for i in range(self._linhas):
			line = ''

			for j in range(self._colunas):
				line += self.verificao_pao_de_queijo(i, j)

			self.escreve_resposta(line)

	def verificao_pao_de_queijo(self, i, j):
		if self.matrix[i][j] == 1:
			return '9'

		else:
			contador = 0
			contador = self.somar_um(contador, i, j - 1)
			contador = self.somar_um(contador, i, j + 1)
			contador = self.somar_um(contador, i - 1, j)
			contador = self.somar_um(contador, i + 1, j)

			return str(contador)

	def somar_um(self, contador, i, j):
		condicao = i >= 0 and j >= 0
		if condicao:
			try:
				if self.matrix[i][j] == 1:
					contador += 1
			except IndexError:
				pass
		return contador

	@staticmethod
	def escreve_resposta(line):
		print(line)


def cheese_bread_sweeper():
	while True:
		try:
			objeto_buscador_pao_de_queijo = BuscadorDePaoDeQueijo()
			objeto_buscador_pao_de_queijo.calcula_numero_chesse_bread()

		except EOFError:
			break


if __name__ == '__main__':
	cheese_bread_sweeper()
