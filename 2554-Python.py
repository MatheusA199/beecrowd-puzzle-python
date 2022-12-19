class Pizza:
    def __init__(self):
        self._num_pessoas, self._num_datas = self.recebe_lista()

    @staticmethod
    def recebe_lista():
        lts = list(map(int, input().split(' ')))
        return lts

    def calcula_data_valida(self):
        data_correta = False
        data_encontro = ''

        for i in range(self._num_datas):
            data, pessoas = self.recebe_datas()

            if data_correta:
                continue
            else:
                if sum(pessoas) == self._num_pessoas:
                    data_encontro = data
                    data_correta = True

        return self.verifica_se_data_palusivel(data_correta, data_encontro)

    @staticmethod
    def recebe_datas():
        lista = list(input().split(' '))
        data = lista[0]
        pessoas = list(map(int, lista[1:]))

        return data, pessoas

    @staticmethod
    def verifica_se_data_palusivel(data_correta, data_encontro):
        if not data_correta:
            return 'Pizza antes de FdI'
        else:
            return str(data_encontro)

    def __str__(self):
        return self.calcula_data_valida()


def pizza_before_bh():

    while True:
        try:
            objeto_pizza = Pizza()
            print(objeto_pizza)

        except EOFError:
            break


if __name__ == '__main__':
    pizza_before_bh()
