class Wifi:
    def __init__(self,entrada):
        self.entrada = entrada
        self.frase = str(self.contagem())

    def contagem(self):
        if self.entrada.count('1') % 2 == 0:
            self.entrada += '0'
            return self.entrada

        else:
            self.entrada += '1'
            return self.entrada

    def __str__(self):
        return self.frase

def parity(Wifi):
    entrada = input()
    objeto = Wifi(entrada)
    print(objeto)

if (__name__ == '__main__'):
    parity(Wifi)