class Caminho:
    def __init__(self,linha, coluna):
        self.linha = linha
        self.coluna = coluna
        self.matriz = self.recebe_matriz()
        self.find_index()

    def recebe_matriz(self):
        matriz = []
        for i in range(self.linha):
            linha = list(map(int, input().split(' ')))
            matriz.append(linha)
        return matriz

    def find_index(self):
        for i, j in enumerate(self.matriz):
            if 1 in j:
                self.index_ash_linha = i
                self.index_ash_coluna = j.index(1)

        for i, j in enumerate(self.matriz):
            if 2 in j:
                self.index_pokemon_linha = i
                self.index_pokemon_coluna = j.index(2)

    def calcula_diferencia(self):
        caminho_linha = abs(self.index_pokemon_linha - self.index_ash_linha)
        caminho_coluna = abs(self.index_pokemon_coluna - self.index_ash_coluna)
        caminho = caminho_coluna + caminho_linha
        return caminho

    def __str__(self):
        return f'{self.calcula_diferencia()}'

def the_last_analogimon():
    while True:
        try:
            linhas, colunas = map(int, input().split(' '))
            objeto_caminho = Caminho(linhas, colunas)
            print(objeto_caminho)

        except EOFError:
            break


if __name__ == '__main__':
    the_last_analogimon()