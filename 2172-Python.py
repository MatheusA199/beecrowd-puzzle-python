class AumentoXp:
    def __init__(self,aumento,valor):
        self.aumento = aumento
        self.valor = valor
        self.acrescimo = self.calculo_aumento()
    
    def calculo_aumento(self):
        acrescimo = self.aumento * self.valor
        return acrescimo

    def __str__(self):
        return f'{self.acrescimo}'    

def event(AumentoXp):
    while True:
        aumento,valor = map(int,input().split(' '))
        if (aumento == 0) and (valor == 0):
            break
        else:
            objeto = AumentoXp(aumento,valor)
            print(objeto)

if (__name__ == '__main__'):
    event(AumentoXp)