class MontanhaRussa:
    def __init__(self):
        self._n_teste, self._alt_min, self._alt_max = self.recebe_lista()

    @staticmethod
    def recebe_numero():
        number = int(input())
        return number

    @staticmethod
    def recebe_lista():
        lts = list(map(int, input().split(' ')))
        return lts

    def calcula_quantas_pessoas_atende_exigencia_altura(self):
        qtn_pessoas = 0
        for i in range(self._n_teste):
            altura = self.recebe_numero()

            altura_valida = self.verifica_se_altura_valida(altura)

            if altura_valida:
                qtn_pessoas += 1

            else:
                pass

        return qtn_pessoas

    def verifica_se_altura_valida(self, altura):
        altura_atende_minimo = altura >= self._alt_min
        altura_atende_maximo = altura <= self._alt_max

        altura_valida = altura_atende_maximo and altura_atende_minimo
        return altura_valida

    def __str__(self):
        resposta = str(self.calcula_quantas_pessoas_atende_exigencia_altura())
        return resposta


def roller_coaster():
    while True:
        try:
            objeto_montanha_russa = MontanhaRussa()
            print(objeto_montanha_russa)

        except EOFError:
            break


if __name__ == '__main__':
    roller_coaster()
