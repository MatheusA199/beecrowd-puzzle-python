class ExameGeral:
    def __init__(self, qtn_notas, qtn_posicao):
        self._qtn_notas = qtn_notas
        self._qtn_posicao = qtn_posicao
        self._notas = self.recebe_notas()

    def recebe_notas(self):
        lts_notas = []

        for i in range(self._qtn_notas):
            lts_notas.append(int(input()))

        return sorted(lts_notas, reverse=True)

    @staticmethod
    def recebe_posicao():
        posicao = int(input())
        return posicao

    def __str__(self):
        posicao = self.recebe_posicao()
        return f'{self._notas[posicao - 1]}'


def general_exam():
    while True:
        try:
            qtn_notas, qtn_posicao = map(int, input().split(' '))
            objeto_exame_geral = ExameGeral(qtn_notas, qtn_posicao)

            for i in range(qtn_posicao):
                print(objeto_exame_geral)

        except EOFError:
            break


if __name__ == '__main__':
    general_exam()