class TouristsInTheHuacachinaPark:

    @staticmethod
    def recebe_entrada():
        entrada = input()
        return entrada
    
    @staticmethod
    def split_itens_entrada(entrada):
        itens = entrada.split()
        return itens
    
    def verifica_quantidades_passageiros(self):
        qtn_passageiros_embarcados = 0
        qtn_jeeps = 0
        while True:
            entrada = self.recebe_entrada()

            if entrada == 'ABEND':
                break
        
            else:
                

                tipo_corrida, qtn_passageiros = self.split_itens_entrada(entrada)

                if tipo_corrida == 'SALIDA':
                    qtn_jeeps += 1
                    qtn_passageiros_embarcados += int(qtn_passageiros)

                elif tipo_corrida == 'VUELTA':
                    qtn_jeeps -= 1
                    qtn_passageiros_embarcados -= int(qtn_passageiros)

        print(qtn_passageiros_embarcados)
        print(qtn_jeeps)


def tourists_in_the_huacachina_park():
    objeto_jeeps = TouristsInTheHuacachinaPark()
    objeto_jeeps.verifica_quantidades_passageiros()

if __name__ == '__main__':
    tourists_in_the_huacachina_park()