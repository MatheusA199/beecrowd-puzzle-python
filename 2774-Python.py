import re

class AjudaPatatatitu:
    def __init__(self) -> None:
        self._qtn_testes = self.recebe_numero()
        # self._lista_compostos_perigosos = self.recebe_compostos_perigosos()

    @staticmethod
    def recebe_entrada():
        entrada = input()
        return entrada
    
    def recebe_numero(self):
        numero = int(self.recebe_entrada())
        return numero

    def recebe_compostos_perigosos(self, qtn_compostos_perigosos):
        lts = []
        for composto in range(qtn_compostos_perigosos):
            lts.append(self.recebe_entrada())

        return lts
    
    def verifica_se_composto_perigoso(self):
        for contador in range(self._qtn_testes):
            qtn_compostos_perigosos = self.recebe_numero()
            lista_compostos_perigosos = self.recebe_compostos_perigosos(qtn_compostos_perigosos)
            qtn_compostos_teste = self.recebe_numero()
            
            for value in range(qtn_compostos_teste):
                perigoso = False
                composto = self.recebe_entrada().strip()
                for composto_perigoso in lista_compostos_perigosos:
                    pattern = f'({composto_perigoso})' + '(?![a-z0-9]{1})'
                    pattern1 = re.compile(pattern)
                    if re.search(pattern1, composto):
                        perigoso = True
                        break
                        
                    else:
                        continue

                if perigoso:
                    print('Abortar')
                
                else:
                    print('Prossiga')
                
            if contador != (self._qtn_testes - 1):
                print('')

def ajuda_patatatitu():
    objeto = AjudaPatatatitu()
    objeto.verifica_se_composto_perigoso()

if __name__ == '__main__':
    ajuda_patatatitu()
