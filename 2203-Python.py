from math import sqrt

class ValidaRange:
    def __init__(self,xf,yf,xi,yi,vi,r1,r2):
        self.delta_x = (xf-xi)**2
        self.delta_y = (yf-yi)**2
        self.distancia = sqrt(self.delta_y + self.delta_x)
        self.velocidade = vi*1.5
        self.range = r1+r2

    def valida_range(self):
        if (self.range >= self.distancia + self.velocidade):
            return 'Y'
        else:
            return 'N'
    
    def __str__(self):
        return self.valida_range()

def crowstorm(ValidaRange):
    while True:
        try:
            xf,yf,xi,yi,vi,r1,r2 = list(map(int,input().split()))
            objeto = ValidaRange(xf,yf,xi,yi,vi,r1,r2)
            print(objeto)
        except EOFError:
            break

if (__name__ == '__main__'):
    crowstorm(ValidaRange)