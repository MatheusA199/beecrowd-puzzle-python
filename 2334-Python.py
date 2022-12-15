class Patinho:
    def __init__(self,entrada) -> None:
        self._patos = entrada
        self._patos_retornam = self.patos_retorna()

    def patos_retorna(self):
        if (self._patos != 0):
            retorna = self._patos - 1
            return retorna
            
        else:
            return 0
    
    def __str__(self) -> str:
        return f'{self._patos_retornam}'

def littler_ducks():
    while True:
        entrada = int(input())
        if entrada == -1:
            break
        else:
            patinho_objeto = Patinho(entrada)
            print(patinho_objeto)

if (__name__ == '__main__'):
    littler_ducks()