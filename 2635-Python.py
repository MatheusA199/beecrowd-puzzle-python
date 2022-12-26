class WebBrowser:
    def __init__(self):
        self._qtn_cache = self.recebe_transforma_entrada()
        self._lista_cache = self.recebe_lista_cache()
        self._qtn_pesquisa = self.recebe_transforma_entrada()

    @staticmethod
    def recebe_entrada():
        entrada = input()
        return entrada

    def recebe_transforma_entrada(self):
        numero = int(self.recebe_entrada())
        return numero

    def recebe_lista_cache(self):
        lts = []

        for i in range(self._qtn_cache):
            pesquisa = self.recebe_entrada()
            lts.append(pesquisa)

        return lts

    def verifica_sugestao(self):
        for i in range(self._qtn_pesquisa):
            pesquisa = self.recebe_entrada()
            sugestao = self.verifica_sugestao_valida(pesquisa)
            self.escreve_resposta(self.verifica_resposta(sugestao))

    def verifica_sugestao_valida(self, pesquisa):
        sugestao = []

        for item in self._lista_cache:
            if pesquisa == item[:len(pesquisa)]:
                sugestao.append(item)

            else:
                continue

        return sugestao

    @staticmethod
    def verifica_resposta(sugestao):

        if len(sugestao) > 0:
            maior_sugestao = max(sugestao, key=len)
            return f'{len(sugestao)} {len(maior_sugestao)}'

        else:
            return '-1'

    @staticmethod
    def escreve_resposta(resposta):
        print(resposta)


def web_browser():
    objeto_web_browser = WebBrowser()
    objeto_web_browser.verifica_sugestao()


if __name__ == '__main__':
    web_browser()