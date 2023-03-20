from math import comb

class DividingCircles:
    def __init__(self) -> None:
        self._number_points = self.recebe_int()

    @staticmethod
    def recebe_int():
        entrada = int(input())
        return entrada
    
    def verifica_qtn_partes(self):
        faces = 1 + comb(self._number_points, 2) + comb(self._number_points, 4)
        return faces
    
    def __str__(self) -> str:
        return str(self.verifica_qtn_partes())
    
def dividing_circles():
    objeto = DividingCircles()
    print(objeto)

if __name__ == '__main__':
    dividing_circles()
 