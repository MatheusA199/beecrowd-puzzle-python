class Partida:
    def __init__(self):
        self._numero_atributos = self.recebe_numero()
        self._n_mao_marcos, self._n_mao_leo = self.recebe_lista()
        self._mao_marcos = self.recebe_mao('marcos')
        self._mao_leo = self.recebe_mao('leo')
        self._carta_marcos, self._carta_leo = list(map(int, input().split(' ')))
        self._atributo = self.recebe_numero() - 1

    @staticmethod
    def recebe_lista():
        lts = list(map(int, input().split()))
        return lts

    @staticmethod
    def recebe_numero():
        numero = int(input())
        return numero

    def recebe_mao(self, jogador):
        if jogador == 'marcos':
            return self.recebe_cartas(self._n_mao_marcos)
        else:
            return self.recebe_cartas(self._n_mao_leo)

    def recebe_cartas(self, n_mao):
        lts = []
        for i in range(n_mao):
            entrada = self.recebe_lista()
            lts.append(entrada)
        return lts

    def verifica_ganhador(self):
        carta_marcos = self._mao_marcos[self._carta_marcos - 1][self._atributo]
        carta_leo = self._mao_leo[self._carta_leo - 1][self._atributo]

        marcos_ganha = carta_marcos > carta_leo
        leo_ganha = carta_marcos < carta_leo

        if marcos_ganha:
            return 'Marcos'

        elif leo_ganha:
            return 'Leonardo'

        else:
            return 'Empate'

    def __str__(self):
        return self.verifica_ganhador()


def lu_di_oh():
    while True:
        try:
            objeto_partida = Partida()
            print(objeto_partida)

        except EOFError:
            break


def recebe_lista():
    lts = list(map(int, input().split(' ')))
    return lts


def recebe_numero():
    numero = int(input())
    return numero


if __name__ == '__main__':
    lu_di_oh()
