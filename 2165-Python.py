class Mensagem:
    def __init__(self,mensagem):
        self.texto = mensagem

    def __str__(self):
        if len(self.texto) > 140:
            return 'MUTE'
        else:
            return 'TWEET'

mensagem = input()
post = Mensagem(mensagem)
print(post)