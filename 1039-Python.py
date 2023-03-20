from math import sqrt

class FireFlowers:
    def __init__(self) -> None:
        self._entrada = self.transform_int_list()


    @staticmethod
    def recebe_entrada():
        entrada = input()
        return entrada
    
    def transform_int_list(self):
        lista_num = list(map(int, self.recebe_entrada().split()))
        return lista_num
    

    def verifica_circulo_correto(self):
        dist_x = self._entrada[1] - self._entrada[4]
        dist_y = self._entrada[2] - self._entrada[5]

        dist_centro_circulos = sqrt((dist_x)**2 + (dist_y) **2)
        distancia_total = dist_centro_circulos + self._entrada[3]
        circ_desenho_valido = distancia_total <= self._entrada[0]

        if circ_desenho_valido:
            return True
        
        else:
            return False

    def __str__(self) -> str:
        rico = self.verifica_circulo_correto()

        if rico:
            return "RICO"
        
        else:
            return "MORTO"
        
def fireflowers():
    while True:
        try:
            flor = FireFlowers()
            print(flor)
        except EOFError:
            break

if __name__ == '__main__':
    fireflowers()
