class Estatisticas:
    def __init__(self,total_saque,total_bloqueio,total_ataque,sucesso_saque,sucesso_bloqueio,sucesso_ataque) -> None:
        self.porcentagem_saque = (sum(sucesso_saque) / sum(total_saque))*100
        self.porcentagem_bloqueio = (sum(sucesso_bloqueio) / sum(total_bloqueio))*100
        self.porcentagem_ataque = (sum(sucesso_ataque) / sum(total_ataque))*100

    def escrever(self):
        print(f'Pontos de Saque: {self.porcentagem_saque:.2f} %.')
        print(f'Pontos de Bloqueio: {self.porcentagem_bloqueio:.2f} %.')
        print(f'Pontos de Ataque: {self.porcentagem_ataque:.2f} %.')

    
def volleyball():
    entrada = int(input())
    total_saque = []
    total_bloqueio = []
    total_ataque = []

    sucesso_saque = []
    sucesso_bloqueio = []
    sucesso_ataque = []

    for i in range(entrada):
        nome = str(input())
        total = list(map(int, input().split(' ')))
        total_saque.append(total[0])
        total_bloqueio.append(total[1])
        total_ataque.append(total[2]) 

        total2 = list(map(int, input().split(' ')))
        sucesso_saque.append(total2[0])
        sucesso_bloqueio.append(total2[1])
        sucesso_ataque.append(total2[2])

    objeto = Estatisticas(total_saque,total_bloqueio,total_ataque,sucesso_saque,sucesso_bloqueio,sucesso_ataque)
    objeto.escrever()

if (__name__ == '__main__'):
    volleyball()