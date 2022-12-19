import math


class Votacao:
    def __init__(self):
        self.qnt_votos = self.recebe_qtn_votos()
        self.votos = self.recebe_votos()

    def calcula_resultado(self):
        minimo_votos = math.ceil((self.qnt_votos / 3) * 2)
        soma_votos = sum(self.votos)

        situacao_impeachment = soma_votos >= minimo_votos
        return situacao_impeachment

    def verifica_impeachment(self):
        situacao_impeachment = self.calcula_resultado()

        if situacao_impeachment:
            return 'impeachment'

        else:
            return 'acusacao arquivada'

    @staticmethod
    def recebe_qtn_votos():
        qtn_votos = int(input())
        return qtn_votos

    @staticmethod
    def recebe_votos():
        votos = list(map(int, input().split(' ')))
        return votos

    def __str__(self):
        resposta = self.verifica_impeachment()
        return resposta


def leaders_impeachment():
    while True:
        try:
            objeto_votacao = Votacao()
            print(objeto_votacao)

        except EOFError:
            break


if __name__ == '__main__':
    leaders_impeachment()
