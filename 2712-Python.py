import re


class VehicularRestriction:
    def __init__(self) -> None:
        self._qtn_veiculos = self.recebe_numero()
        self._dict_dias = {
            'MONDAY' : [1, 2],
            'TUESDAY' : [3, 4],
            'WEDNESDAY' : [5, 6],
            'THURSDAY' : [7, 8],
            'FRIDAY' : [9, 0]
        }

    @staticmethod
    def recebe_numero():
        numero = int(input())
        return numero
    
    def verifica_dia_circulacao_carro(self):

        for i in range(self._qtn_veiculos):
            placa = input()
            placa_valida = self.verifica_se_placa_valida(placa)

            if placa_valida:
                dia_semana = self.verifica_dia_da_semana(placa)
                print(dia_semana, end='\n')
            
            else:
                print('FAILURE')

    @staticmethod
    def verifica_se_placa_valida(placa):
        pattern = re.compile("([A-Z]{3})(-)([0-9]{4})")
        if re.match(pattern, placa) and len(placa) == 8:
            return True

        else:
            return False

    def verifica_dia_da_semana(self, placa):
        ultimo_numero = int(placa[-1])
        for key, item in self._dict_dias.items():
            if ultimo_numero == item[0] or ultimo_numero == item[1]:
                dia = key
                break
        return dia


def vehicular_restriction():
    objeto = VehicularRestriction()
    objeto.verifica_dia_circulacao_carro()


if __name__ == '__main__':
    vehicular_restriction()        
