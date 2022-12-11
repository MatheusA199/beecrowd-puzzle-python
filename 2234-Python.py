class TaxaConsumo:
    def __init__(self,consumo, participantes) -> None:
        self.consumo = consumo
        self.participantes = participantes
        self.indice = self.calculo_indice()

    def calculo_indice(self):
        valor = self.consumo / self.participantes
        taxa = round(valor,2)
        return taxa
    
    def __str__(self) -> str:
        return f'{self.indice:.2f}'

def hot_dogs(TaxaConsumo):
    consumo, participantes = map(int, input().split(' '))
    objeto = TaxaConsumo(consumo, participantes)
    print(objeto)

if (__name__ ==  '__main__'):
    hot_dogs(TaxaConsumo)