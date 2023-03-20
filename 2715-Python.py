class  SplittingAssignmentsI:
    def __init__(self) -> None:
        self._qtn_assignment = self.recebe_int()
        self._lts_assigment = self.transforma_entrada_valores_int_lista()
        self._soma_dificuldades = sum(self._lts_assigment)

    def encontra_equilibrio_distribuicao_dificuldade(self) -> int:
        soma_dificuldade_rangel = 0
        contador = 0 

        for value in self._lts_assigment:
            soma_dificuldade_rangel += value
            soma_dificuldade_gugu = abs(self._soma_dificuldades - soma_dificuldade_rangel)
            menor_diferencia_temporaria = abs(soma_dificuldade_gugu - soma_dificuldade_rangel)

            if contador == 0:
                menor_diferencia = menor_diferencia_temporaria
                contador += 1
            
            elif menor_diferencia_temporaria < menor_diferencia:
                menor_diferencia = menor_diferencia_temporaria
            
            elif menor_diferencia_temporaria > menor_diferencia:
                return menor_diferencia

    def __str__(self) -> str:
        menor_diferencia = self.encontra_equilibrio_distribuicao_dificuldade()
        return str(menor_diferencia)

    @staticmethod
    def recebe_entrada() -> str:
        entrada = input()
        return entrada

    def recebe_int(self) -> int:
        numero = int(self.recebe_entrada())
        return numero
    
    def transforma_entrada_valores_int_lista(self) -> list:
        entrada = self.recebe_entrada()
        lts_assigment = list(map(int, entrada.split()))
        return lts_assigment
    

def splitting_assignmentsI():
    while True:
        try:
            objeto = SplittingAssignmentsI()
            print(objeto)

        except EOFError:
            break


if __name__ == '__main__':
    splitting_assignmentsI()