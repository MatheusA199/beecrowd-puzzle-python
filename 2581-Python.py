class Toorg:
    def __init__(self):
        self._qnt_teste = self.recebe_transforma_int()

    @staticmethod
    def recebe_entrada():
        entrada = input()
        return entrada

    def recebe_transforma_int(self):
        entrada = int(self.recebe_entrada())
        return entrada

    def gera_resposta(self):
        for i in range(self._qnt_teste):
            pergunta = self.recebe_entrada()
            self.escreve_i_am_toorg()

    @staticmethod
    def escreve_i_am_toorg():
        print('I am Toorg!')


def i_am_toorg():
    objeto_toorg = Toorg()
    objeto_toorg.gera_resposta()


if __name__ == '__main__':
    i_am_toorg()
