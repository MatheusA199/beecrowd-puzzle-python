class NovoRecorde:
    def __init__(self):
        self._teste = self.recebe_numero()
        self._record = 0

    @staticmethod
    def recebe_numero():
        number = int(input())
        return number

    @staticmethod
    def recebe_lista():
        lts = list(map(int, input().split(' ')))
        return lts

    def calcula_quantas_vezes_recorde_quebrado(self):
        for i in range(self._teste):
            tempo, distancia = self.recebe_lista()
            recorde = distancia / tempo

            quebrou_recorde = recorde > self._record

            if quebrou_recorde:
                dia = i + 1
                self._record = recorde
                print(dia)

            else:
                pass


def new_record():
    while True:
        try:
            objeto_novo_recorde = NovoRecorde()
            objeto_novo_recorde.calcula_quantas_vezes_recorde_quebrado()
        except EOFError:
            break


if __name__ == '__main__':
    new_record()
