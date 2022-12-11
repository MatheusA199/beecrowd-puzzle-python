class Testes:
    def __init__(self,teste_feitos, velocidade):
        self.testes_feitos = teste_feitos
        self.valores= velocidade
        self.ocorrencia = self.verificacao()

    def verificacao(self):
        value = 0
        for i in range(1,len(self.valores)):
            if self.valores[i] >= self.valores[i-1]:
                pass
            else:
                value = i+1
                return value
        return value

    def __str__(self):
        return f'{self.ocorrencia}'

def engine_failure():
    teste_feitos = int(input())
    velocidades = list(map(int,input().split(' ')))
    teste = Testes(teste_feitos,velocidades)
    print(teste)

if (__name__ == '__main__'):
    engine_failure()