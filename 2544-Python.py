class JutsuClonedasSombras:
    def __init__(self):
        self._numero_ninjas = self.recebe_numero()

    @staticmethod
    def recebe_numero():
        numero = int(input())
        return numero

    def calcula_qtn_jutsus(self):
        contador = 0
        while True:
            numero_ninjas_maior_que_um = self._numero_ninjas > 1

            if numero_ninjas_maior_que_um:
                self._numero_ninjas //= 2
                contador += 1
            else:
                break

        return contador

    def __str__(self):
        resposta = str(self.calcula_qtn_jutsus())
        return resposta


def kage_bunshin_no_jutsu():
    while True:
        try:
            objeto_jutsu_clone = JutsuClonedasSombras()
            print(objeto_jutsu_clone)
        except EOFError:
            break


if __name__ == '__main__':
    kage_bunshin_no_jutsu()
