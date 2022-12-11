class Duelo:
    def __init__(self,bonus,dados_dagriel,dados_guarte):
        self.bonus = bonus
        self.pontos_dagriel = self.calcula_pontos(dados_dagriel,bonus)
        self.pontos_guarte = self.calcula_pontos(dados_guarte,bonus)

    def calcula_pontos(self,dados,bonus):
        pontos = (dados[0] + dados[1])/2
        if dados[2] % 2 == 0:
            pontos += bonus
        return pontos
        
    def valida_ganhador(self):
        if self.pontos_guarte > self.pontos_dagriel:
            return "Guarte"
        
        elif self.pontos_guarte < self.pontos_dagriel:
            return "Dabriel"
        
        else:
            return "Empate"

    def __str__(self):
        return self.valida_ganhador()

def pomekons_Battle(Duelo):
    entrada = int(input())

    for i in range(entrada):
        bonus = int(input())
        dados_guarte = list(map(int,input().split(' ')))
        dados_dagriel = list(map(int,input().split(' ')))

        objeto = Duelo(bonus,dados_guarte,dados_dagriel)
        print(objeto)
    
if (__name__ == '__main__'):
    pomekons_Battle(Duelo)