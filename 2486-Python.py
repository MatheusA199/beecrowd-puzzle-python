class Itens(object):
    def __init__(self) -> None:
        self.items = {
            'suco de laranja': 120,
            'morango fresco': 85,
            'mamao': 85,
            'goiaba vermelha': 70,
            'manga': 56,
            'laranja': 50,
            'brocolis': 34,
        }

    def verifica_item(self,entrada):
        self.valor = self.items.get(entrada,'Deu erro')
        return self.valor

class VitaminaC(Itens):
    def __init__(self,entrada) -> None:
        self.entrada = entrada
        self.resposta = 0
        super().__init__()
        

    def recebe_entrada(self):
        for i in range(self.entrada):
            entrada = input().split()
            consumo = int(entrada[0])
            item = ' '.join(entrada[1:])
            valor = super().verifica_item(item)
            quantidade = valor * consumo
            self.resposta += quantidade
    
    def valida_quantidade(self):
        consumo_menor = self.resposta <110
        consumo_maior = self.resposta > 130

        if consumo_menor:
            diferencia = 110 - self.resposta
            return f'Mais {diferencia} mg'

        elif consumo_maior:
            diferencia = self.resposta - 130
            return f'Menos {diferencia} mg'    

        else:
            return f'{self.resposta} mg'

    def __str__(self) -> str:
        return self.valida_quantidade()

class Programa(VitaminaC):
    def __init__(self) -> None:
        while True:
            entrada = int(input())
            if (entrada != 0):
                objeto_vitaminac = VitaminaC(entrada)
                objeto_vitaminac.recebe_entrada()
                print(objeto_vitaminac)
            else:
                break

def c_mais_ou_menos():
    objeto = Programa()

if (__name__ == '__main__'):
    c_mais_ou_menos()
