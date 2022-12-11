class Matriz:
    def __init__(self,entrada,matriz):
        self.entrada = entrada
        self.matriz = matriz
        self.resposta = self.verificacao()

    def verificacao(self):
        frase = ''
        for i in range(self.entrada):
            for j in range(self.entrada):
                ver = (self.matriz[i][j] + self.matriz[i][j+1] + self.matriz[i+1][j] + self.matriz[i+1][j+1] < 2)
                if (ver):
                    frase += ('U')
                else:
                    frase += ('S')
        return frase

    @property
    def escrever(self):
        for i in range(0,len(self.resposta),self.entrada):
            print(self.resposta[i:i+self.entrada])

def twilight_at_portland(Matriz):

    entrada = int(input())
    lista = []
    for i in range(entrada+1):
        valores = list(map(int,input().split(' ')))
        lista.append(valores)
    objeto = Matriz(entrada,lista)
    objeto.escrever

if (__name__ == '__main__'):
    twilight_at_portland(Matriz)