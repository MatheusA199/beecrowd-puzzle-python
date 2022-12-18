class Mensagem:
    def __init__(self, mensagem, letras):
        self.mensagem = mensagem
        self.letras_index = letras

    def encontra_mensagem(self):
        mensagem_final = ''
        for i in self.letras_index:
            mensagem_final += self.mensagem[i-1]

        return mensagem_final

    def __str__(self):
        mensagem_final = self.encontra_mensagem()
        return f'{mensagem_final}'

def wills_message():
    while True:
        try:
            mensagem = input()
            tamanho = int(input())
            letras = list(map(int, input().split(' ')))
            objeto_mensagem = Mensagem(mensagem, letras)
            print(objeto_mensagem)

        except EOFError:
            break

if __name__ == '__main__':
    wills_message()