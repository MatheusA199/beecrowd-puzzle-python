class OperationGame:
    def __init__(self,entrada) -> None:
        self.entrada = entrada
        self.respostas = self.recebe_equacao()
        self.nomes_erraram = self.recebe_palpite()

    def recebe_equacao(self):
        resposta = []
        for i in range(self.entrada):
            equacao = input().strip().replace('=',' ')
            equacao = list(map(int,equacao.split(' ')))

            verifica_soma = (equacao[0] + equacao[1] == equacao[2])
            verifica_sub = (equacao[0] - equacao[1] == equacao[2])
            verifica_mult = (equacao[0] * equacao[1] == equacao[2])

            if (verifica_soma):
                resposta.append('+')
            
            elif (verifica_sub):
                resposta.append('-')

            elif (verifica_mult):
                resposta.append('*')
            
            else:
                resposta.append('I')
            
        return resposta

    def recebe_palpite(self):
        nomes_erraram = []
        for i in range(self.entrada):
            palpite = input().strip().split(' ')
            nome = palpite[0]
            eq = int(palpite[1]) - 1
            simbolo = palpite[2]

            palpite_errado = (simbolo != self.respostas[eq])

            if palpite_errado:
                nomes_erraram.append(nome)
            
            else:
                pass
        
        return sorted(nomes_erraram)
        
    def __str__(self) -> str:
        todos_erraram = (len(self.nomes_erraram) == self.entrada)
        todos_acertaram = (len(self.nomes_erraram) == 0)

        if todos_acertaram:
            return 'You Shall All Pass!'

        elif todos_erraram:
            return 'None Shall Pass!'

        else:
            nome_alfa = self.nomes_erraram
            saida = ' '.join(nome_alfa[0:])
            return saida

def jogo_do_operador():
    while True:
        try:
            entrada = int(input().strip())
            objeto_jogo_operacoes = OperationGame(entrada)
            print(objeto_jogo_operacoes)

        except EOFError:
            break

if (__name__ == '__main__'):
    jogo_do_operador()