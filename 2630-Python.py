import math


class Greyscale:
    def __init__(self):
        self._qtn_teste = self.transforma_em_int()

    @staticmethod
    def recebe_entrada():
        entrada = input()
        return entrada

    def transforma_em_int(self):
        numero = int(self.recebe_entrada())
        return numero

    def transforma_em_str(self):
        linha = str(self.recebe_entrada())
        return linha

    @staticmethod
    def transforma_em_lista_converte_inteiro():
        lts = list(map(int, input().split()))
        return lts

    def realica_recebe_resultado_escreve(self):
        for value in range(self._qtn_teste):
            p = self.realiza_calculo_nivel_cinza()
            self.escrever_resposta(value, p)

    @staticmethod
    def escrever_resposta(value, p):
        print(f'Caso #{value + 1}: {p}')

    def realiza_calculo_nivel_cinza(self):
        tipo_conversao = self.transforma_em_str()
        lista_rgb = self.transforma_em_lista_converte_inteiro()
        p = 0

        if tipo_conversao == 'min':
            p = min(lista_rgb)

        elif tipo_conversao == 'mean':
            p = sum(lista_rgb) / len(lista_rgb)

        elif tipo_conversao == 'max':
            p = max(lista_rgb)

        elif tipo_conversao == 'eye':
            p = lista_rgb[0] * 0.3 + lista_rgb[1] * 0.59 + lista_rgb[2] * 0.11

        return math.floor(p)


def greyscale():
    objeto_greyscale = Greyscale()
    objeto_greyscale.realica_recebe_resultado_escreve()


if __name__ == '__main__':
    greyscale()
