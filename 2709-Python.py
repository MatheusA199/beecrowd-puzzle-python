class TheCoinsOfRobbie:
    def __init__(self) -> None:
        self._number_coins = self.recebe_numero()
        self._values_coins = self.recebe_valores_moedas()
        self._jumps = self.recebe_numero()

    def recebe_numero(self):
        numero = int(input())
        return numero
    
    def recebe_valores_moedas(self):
        values_coins = [self.recebe_numero() for i in range(0, self._number_coins)]
        return values_coins
    
    def calcula_soma_valores_moedas(self):
        soma = 0
        for value in range(len(self._values_coins), 0, -self._jumps):
            soma = soma + self._values_coins[value - 1]
        
        return soma
    
    def verifica_ganhador(self):
        soma = self.calcula_soma_valores_moedas()
        numero_primo = True

        if soma == 1: 
            numero_primo = False
        
        elif soma == 2:
            pass

        elif soma % 2 == 0:
            numero_primo = False

        else:
            for value in range(3, (soma // 2) + 1, 2):
                if soma % value == 0:
                    numero_primo = False
                    break
            
                else:
                    pass
        return numero_primo
    
    def __str__(self) -> str:
        numero_primo = self.verifica_ganhador()
        
        if numero_primo == False:
            return r'Bad boy! I’ll hit you.'
        
        else:
            return r'You’re a coastal aircraft, Robbie, a large silver aircraft.'

def the_coins_of_robbie():
    while True:
        try:
            objeto_the_coins_of_robbie = TheCoinsOfRobbie()
            print(objeto_the_coins_of_robbie)
        
        except EOFError:
            break
    
if __name__ == '__main__':
    the_coins_of_robbie()

