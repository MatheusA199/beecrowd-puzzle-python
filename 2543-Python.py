class Gaming:
    def __init__(self):
        self._qtn_video, self._id_jogador = self.recebe_entrada()

    @staticmethod
    def recebe_entrada():
        lts = list(map(int, input().split(' ')))
        return lts

    def calcula_qtn_video(self):
        qtn_cs_video_do_id_certo = 0

        for i in range(self._qtn_video):
            gameplay_cs_do_id_certo = self.verifica_gameplay_certo()
            if gameplay_cs_do_id_certo:
                qtn_cs_video_do_id_certo += 1
            else:
                pass

        return qtn_cs_video_do_id_certo

    def verifica_gameplay_certo(self):
        id_jogador, tipo_jogo = self.recebe_entrada()
        he_id_jogador = self._id_jogador == id_jogador
        he_cs = tipo_jogo == 0

        return he_id_jogador and he_cs

    def __str__(self):
        qtn_video = str(self.calcula_qtn_video())
        return qtn_video


def ufrp_gaming():
    while True:
        try:
            objeto_gaming = Gaming()
            print(objeto_gaming)

        except EOFError:
            break


if __name__ == '__main__':
    ufrp_gaming()