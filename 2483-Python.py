class MerryChristmas:
    def __init__(self) -> None:
        self.entrada = self.recebe_entrada()
        self.repeticao = self.calculo_repeticao()
        pass

    def calculo_repeticao(self):
        repeticao = 'a'*self.entrada
        return repeticao
    
    def recebe_entrada(self):
        entrada = int(input())
        return entrada

    def __str__(self) -> str:
        return 'Feliz '+'nat'+self.repeticao+'l!'

def merry_christmas():
    objeto_feliz_natal = MerryChristmas()
    print(objeto_feliz_natal)

if (__name__ == '__main__'):
    merry_christmas()