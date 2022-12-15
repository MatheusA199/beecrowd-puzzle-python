class NotasDaProva:
    def __init__(self) -> None:
        self.nota = self.recebe_entrada()
        pass

    def verifica_conceito(self):
        conceito_e = (self.nota == 0)
        conceito_d = (1 <= self.nota and self.nota <= 35)
        conceito_c = (36 <= self.nota and self.nota <= 60)
        conceito_b = (61 <= self.nota and self.nota <=85)
        conceito_a = (86 <= self.nota and self.nota <= 100)

        if conceito_e:
            return 'E'

        elif conceito_d:
            return 'D'

        elif conceito_c:
            return 'C'
        
        elif conceito_b:
            return 'B'
        
        elif conceito_a:
            return 'A'

    def __str__(self) -> str:
        return self.verifica_conceito()

    def recebe_entrada(self):
        entrada = int(input())
        return entrada

def notas_de_provas():
    objeto_nota_de_prova = NotasDaProva()
    print(objeto_nota_de_prova)

if (__name__ == '__main__'):
    notas_de_provas()