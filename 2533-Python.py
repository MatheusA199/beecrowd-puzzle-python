class Estagio:
    def __init__(self):
        self.entrada = int(input())

    def recebe_entradas(self):
        somatoria_c = 0
        somatoria_n_c = 0

        for i in range(self.entrada):
            n, c = map(int, input().split(' '))
            somatoria_c += c
            somatoria_n_c += c * n

        return somatoria_c, somatoria_n_c

    def calcula_resultado(self):
        somatoria_c, somatoria_n_c = self.recebe_entradas()

        resposta = somatoria_n_c / (somatoria_c * 100)

        return resposta

    def __str__(self):
        resposta = self.calcula_resultado()
        return f'{resposta:.4f}'

def internship():
    while True:
        try:
            objeto_estagio = Estagio()
            print(objeto_estagio)

        except EOFError:
            break

if __name__ == '__main__':
    internship()
