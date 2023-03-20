class Fase:
    def __init__(self):
        self._qtn_competidores = self.recebe_entrada_transforma_int()
        self._qtn_vagas = self.recebe_entrada_transforma_int()
        self._lista_nota = self.recebe_lista()

    def calcula_numero_aprovados(self):
        qtn_aprovados = 0

        for value in range(self._qtn_vagas):
            if value == self._qtn_vagas - 1:
                contador = 1
                maior_referencia = self._lista_nota[value]
                indice_nota = value + contador
                indice_for_valido = indice_nota < len(self._lista_nota)
                while True:
                    try:
                        if self._lista_nota[indice_nota] == maior_referencia:
                            qtn_aprovados += 1
                            contador += 1

                        else:
                            break
                    except:
                        break
            else:
                qtn_aprovados += 1

        return qtn_aprovados

    def __str__(self):
        return str(self.calcula_numero_aprovados())

    def recebe_lista(self):
        lista = [self.recebe_entrada_transforma_int() for i in range(self._qtn_competidores)]
        lista.sort(reverse=True)
        return lista

    @staticmethod
    def recebe_entrada():
        entrada = input()
        return entrada

    def recebe_entrada_transforma_int(self):
        numero = int(self.recebe_entrada())
        return numero


def fase():
    objeto_fase = Fase()
    print(objeto_fase)


if __name__ == '__main__':
    fase()
