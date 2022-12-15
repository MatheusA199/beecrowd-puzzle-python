class PontosSalto:
    def __init__(self) -> None:
        self.entrada = self.recebe_entrada
        self.calculo()


    def calculo(self):
        for i in range(self.entrada):
            self.nome = self.recebe_nome
            self.dificuldade = self.recebe_dificuldade
            self.notas = self.recebe_notas

            self.excluir_menor_nota()
            self.excluir_maior_nota()

            self.nota_final = self.calcular_nota()

            self.escrever()

    @property
    def recebe_entrada(self):
        entrada = int(input())
        return entrada
    
    @property
    def recebe_dificuldade(self):
        entrada = float(input())
        return entrada
    
    @property
    def recebe_nome(self):
        nome = str(input())
        return nome
    
    @property
    def recebe_notas(self):
        notas = list(map(float,input().split(' ')))
        return notas 

    def excluir_menor_nota(self):
        valor_minimo = min(self.notas)
        self.notas.remove(valor_minimo)

    def excluir_maior_nota(self):
        valor_maximo = max(self.notas)
        self.notas.remove(valor_maximo)

    def calcular_nota(self):
        nota_final = sum(self.notas)* self.dificuldade
        return nota_final

    def escrever(self):
        print(f'{self.nome} {self.nota_final:.2f}')

def diving():
    pontos_salto_objeto = PontosSalto()

if (__name__ == '__main__'):
    diving()