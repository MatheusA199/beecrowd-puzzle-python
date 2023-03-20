from time import strftime, gmtime


class TheChangeContinues:
    def __init__(self) -> None:
        self._position = self.recebe_float()

    def recebe_float(self):
        numero = float(input())
        return numero
    
    def verifica_hora_do_dia(self):
        manha = 0 <= self._position < 90 or self._position == 360
        tarde = 90 <= self._position < 180
        noite = 180 <= self._position < 270
        madrugada = 270 <= self._position < 360
        horario = self.calcula_horario()

        if manha:
            mensagem = 'Bom Dia!!'
        
        elif tarde:
            mensagem = 'Boa Tarde!!'

        elif noite:
            mensagem = 'Boa Noite!!'
        
        elif madrugada:
            mensagem = 'De Madrugada!!'

        return mensagem, horario
    
    def calcula_horario(self):
        unidade = 360 / 86400
        qtn_segundo = (self._position / unidade) + (6 * 3600)
        horario = strftime(r"%H:%M:%S", gmtime(qtn_segundo))
        return horario

    def escrever_resposta(self):
        mensagem, horario = self.verifica_hora_do_dia()
        print(mensagem)
        print(horario)

def the_change_continues():
    while True:
        try:
            objeto_the_change_continues = TheChangeContinues()
            objeto_the_change_continues.escrever_resposta()

        except EOFError:
            break
    
if __name__ == '__main__':
    the_change_continues()