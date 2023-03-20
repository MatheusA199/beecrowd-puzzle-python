class Dijkstra:
    def __init__(self):
        self._lista_tipo = []

    @staticmethod
    def recebe_entrada():
        entrada = input()
        return entrada

    def recebe_tipo_jewel(self):
        entrada = self.recebe_entrada()
        if entrada in self._lista_tipo:
            pass
        else:
            self._lista_tipo.append(entrada)

    def verifica_qtn_tipo(self):
        num_tipo = len(set(self._lista_tipo))
        return num_tipo

    def __str__(self):
        return str(self.verifica_qtn_tipo())


def dijkstra():
    obj_dijkstra = Dijkstra()
    while True:
        try:
            obj_dijkstra.recebe_tipo_jewel()
        except EOFError:
            break

    print(obj_dijkstra)


if __name__ == '__main__':
    dijkstra()
