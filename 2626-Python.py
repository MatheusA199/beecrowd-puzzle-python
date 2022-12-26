class Jb6Team:
    def __init__(self):
        self.resposta = self.recebe_entrada_lista()
        self.empate = self.verifica_empate()
        self.jogador_ganhador = -1

        self.dicionario_ganho = {
            'papel': 'pedra',
            'pedra': 'tesoura',
            'tesoura': 'papel',
        }

    @staticmethod
    def recebe_entrada_lista():
        resposta = input().split()
        return resposta

    def verifica_empate(self):
        todos_iguais = all(element == self.resposta[0] for element in self.resposta)
        qtn_pedra = self.contagem('pedra')
        qtn_papel = self.contagem('papel')
        qtn_tesoura = self.contagem('tesoura')
        todos_diferentes = qtn_pedra == qtn_papel == qtn_tesoura

        if todos_diferentes or todos_iguais:
            return True
        else:
            return False

    def contagem(self, entrada):
        qtn = self.resposta.count(entrada)
        return qtn

    def verifica_resultado_patida(self):
        i = 1
        if self.empate:
            pass

        else:
            for key, value in self.dicionario_ganho.items():
                if self.jogador_ganhador == -1:
                    if self.resposta[i] == self.resposta[i - 1]:
                        self.verifica_ganhador(i + 1, i, key, value)

                    elif self.resposta[i + 1] == self.resposta[i]:
                        self.verifica_ganhador(i - 1, i, key, value)

                    elif self.resposta[i - 1] == self.resposta[i + 1]:
                        self.verifica_ganhador(i, i + 1, key, value)
                else:
                    break

    def verifica_ganhador(self, i, j, key, value):
        if self.resposta[i] == key and self.resposta[j] == value:
            self.jogador_ganhador = i

    def __str__(self):
        if self.jogador_ganhador != -1:
            if self.jogador_ganhador == 0:
                return 'Os atributos dos monstros vao ser inteligencia, sabedoria...'

            elif self.jogador_ganhador == 1:
                return "Iron Maiden's gonna get you, no matter how far!"

            elif self.jogador_ganhador == 2:
                return "Urano perdeu algo muito precioso..."
        else:
            return 'Putz vei, o Leo ta demorando muito pra jogar...'


def bg6_team():
    while True:
        try:
            objeto_team = Jb6Team()
            objeto_team.verifica_resultado_patida()
            print(objeto_team)

        except EOFError:
            break


if __name__ == '__main__':
    bg6_team()
