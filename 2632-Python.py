import math


class MagicAndSword:
    def __init__(self):
        self._qtn_teste = self.transforma_em_int()
        self._dict_jogo = {
            'fire':  {'dmg': 200, 1: 20, 2: 30, 3: 50},
            'water': {'dmg': 300, 1: 10, 2: 25, 3: 40},
            'earth': {'dmg': 400, 1: 25, 2: 55, 3: 70},
            'air':   {'dmg': 100, 1: 18, 2: 38, 3: 60}
        }

    def calcula_se_range_spell_valido(self):
        for i in range(self._qtn_teste):
            entrada = self.trasforma_em_lista()

            width, height, quadrado_x0, quadrado_y0 = self.retorna_lista_como_int(entrada)
            tipo_spell, nivel, centro_x0, centro_y0 = self.retorna_tipo_spell_nivel_centro_circulo()

            dados_spell = self._dict_jogo[tipo_spell]
            dano_qtn = dados_spell['dmg']
            raio = dados_spell[nivel]

            limite_x = self.verifica_se_circ_dentro_quad(quadrado_x0, centro_x0, width)
            limite_y = self.verifica_se_circ_dentro_quad(quadrado_y0, centro_y0, height)
            centro_dentro_quadrado = limite_x and limite_y

            if centro_dentro_quadrado:
                range_valido = True

            else:
                delta_qrad_circ_y0 = (quadrado_y0 - centro_y0) ** 2
                delta_mais_h_circ_y0 = (quadrado_y0 + height - centro_y0) ** 2

                delta_quadrado_lado = quadrado_x0 + width + 1

                self.verifica_se_range_e_valido(delta_quadrado_lado, quadrado_x0, centro_x0, delta_qrad_circ_y0, delta_mais_h_circ_y0, raio)

                delta_qrad_circ_x0 = (quadrado_x0 - centro_x0) ** 2
                delta_mais_h_circ_x0 = (quadrado_x0 + width - centro_x0) ** 2

                delta_quadrado_lado_y = quadrado_y0 + height + 1

                range_valido = self.verifica_se_range_e_valido(delta_quadrado_lado_y, quadrado_y0, centro_y0, delta_qrad_circ_x0, delta_mais_h_circ_x0, raio)
            self.escrever_respostas(range_valido, dano_qtn)

    def verifica_se_range_e_valido(self, delta_quadrado_lado, lado_quadrado, centro_circ, distancia_cir, delta_cir_mais_lado, raio):
        for ponto_x in range(lado_quadrado, delta_quadrado_lado):
            distancia_minima = math.sqrt((ponto_x - centro_circ) ** 2 + distancia_cir)
            distancia_maxima = math.sqrt((ponto_x - centro_circ) ** 2 + delta_cir_mais_lado)

            range_valido = self.verifica_raio_valido(raio, distancia_minima, distancia_maxima)
            if range_valido:
                return range_valido

    @staticmethod
    def escrever_respostas(range_valido, dano_qtn):
        if range_valido:
            print(dano_qtn)

        else:
            print(0)

    @staticmethod
    def verifica_raio_valido(raio, distancia_minima, distancia_maxima):
        if raio >= distancia_minima or raio >= distancia_maxima:
            return True

    @staticmethod
    def recebe_entrada():
        entrada = input()
        return entrada

    @staticmethod
    def retorna_lista_como_int(valores):
        lista_int = list(map(int, valores))
        return lista_int

    def trasforma_em_lista(self):
        lista = list(self.recebe_entrada().split())
        return lista

    def transforma_em_int(self):
        numero = int(self.recebe_entrada())
        return numero

    def retorna_tipo_spell_nivel_centro_circulo(self):
        lts = self.trasforma_em_lista()
        spell = lts[0]
        nivel, centro_x0, centro_y0 = self.retorna_lista_como_int(lts[1:])
        return spell, nivel, centro_x0, centro_y0

    @staticmethod
    def verifica_se_circ_dentro_quad(lado_quadrado, centro, aumento):
        limite = lado_quadrado <= centro <= lado_quadrado + aumento
        return limite

def magic_and_sword():
    objeto_magic_and_sword = MagicAndSword()
    objeto_magic_and_sword.calcula_se_range_spell_valido()


if __name__ == '__main__':
    magic_and_sword()
