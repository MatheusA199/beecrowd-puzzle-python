class MusicasPlayList:
    def __init__(self):
        self.playlist = {
            0: 'PROXYCITY',
            1: 'P.Y.N.G.',
            2: 'DNSUEY!',
            3: 'SERVERS',
            4: 'HOST!',
            5: 'CRIPTONIZE',
            6: 'OFFLINE DAY',
            7: 'SALT',
            8: 'ANSWER!',
            9: 'RAR?',
            10: 'WIFI ANTENNAS',
        }

    def retorna_musica_selecionada(self, faixa_selecionada):
        musica = self.playlist.get(faixa_selecionada)
        return musica


class Cd(MusicasPlayList):
    def __init__(self):
        super().__init__()
        self._qtn_testes = self.recebe_numero()

    @staticmethod
    def recebe_numero():
        numero = int(input())
        return numero

    @staticmethod
    def recebe_lista_transforma_int():
        lts = list(map(int, input().split()))
        return lts

    def laco_escreve_cada_musica_selecionada(self):
        for i in range(self._qtn_testes):
            faixa_selecionada = self.retornar_faixa_selecionada()

            musica_selecionada = self.retorna_musica_selecionada(faixa_selecionada)

            self.escreve_musica_selecionada(musica_selecionada)

    def retornar_faixa_selecionada(self):
        valores = self.recebe_lista_transforma_int()
        faixa_selecionada = self.calcula_soma_valores_lista_valores(valores)
        return faixa_selecionada

    @staticmethod
    def calcula_soma_valores_lista_valores(valores):
        soma_valores = sum(valores)
        return soma_valores

    @staticmethod
    def escreve_musica_selecionada(musica_selecionada):
        print(musica_selecionada)


def system_of_a_download():
    objeto_cd_system_of_a_dowload = Cd()
    objeto_cd_system_of_a_dowload.laco_escreve_cada_musica_selecionada()


if __name__ == '__main__':
    system_of_a_download()
