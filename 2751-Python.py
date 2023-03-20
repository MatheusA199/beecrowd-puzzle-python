class IndecisionOfReindeers:
    def __init__(self) -> None:
        self._dict_winner = {
            1 : 'Dasher',
            2 : 'Dancer',
            3 : 'Prancer',
            4:  'Vixen',
            5 : 'Comet',
            6 : 'Cupid',
            7 : 'Donner',
            8 : 'Blitzen',
            0 : 'Rudolph',
        }
        self._list_numbers = self.recebe_list_transforma_int()
        self._sum_snowballs = sum(self._list_numbers)

    def recebe_list_transforma_int(self):
        lista_numeros = list(map(int, input().split()))
        return lista_numeros

    def calcula_winner(self):
        resto = self._sum_snowballs % 9
        ganhador = self._dict_winner[resto]
        return ganhador
    
    def __str__(self) -> str:
        return self.calcula_winner()
    
def indecision_of_reindeers():
    objeto_snowball = IndecisionOfReindeers()
    print(objeto_snowball)

if __name__ == "__main__":
    indecision_of_reindeers()