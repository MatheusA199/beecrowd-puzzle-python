class Criptografia:
    def __init__(self, cifra_len, mensagens, cifra1, cifra2):
        self._cifra_len = cifra_len
        self._mensagens = mensagens
        self._cifra_final = self.retornar_dicionario_cifra_final(cifra1, cifra2)
        #self._keys = self._cifra_final.keys()
        self._puzzle = ''
        self._mensagem_decifrada = ''

    def retornar_dicionario_cifra_final(self, cifra1, cifra2):
        lts1 = [letter for letter in cifra1]
        lts2 = [letter for letter in cifra2]
        lts_um = lts1 + lts2
        lts_dois = lts2 + lts1
        cifra_final = dict(zip(lts_dois, lts_um))
        return cifra_final

    def set_recebe_puzzle(self, novo_puzzle):
        self._puzzle = novo_puzzle

    def desencriptar(self):
        mensagem = ''

        for letter in self._puzzle:
            ver1 = letter.lower() in self._cifra_final.keys()
            if ver1:
                ver2 = letter == letter.upper() and letter != letter.lower()
                if ver2:
                    key = letter.lower()
                    mensagem += self._cifra_final[key].upper()

                else:
                    key = letter.lower()
                    mensagem += self._cifra_final[key].lower()

            else:
                mensagem += letter

        return mensagem

    def __str__(self):
        self._mensagem_decifrada = self.desencriptar()
        return f'{self._mensagem_decifrada}'


def deciphering_the_encrypted_card():
    while True:
        try:
            cifra_len, mensagens = map(int, input().split(' '))
            cifra1 = input().lower()
            cifra2 = input().lower()
            objeto_criptografia = Criptografia(cifra_len, mensagens, cifra1, cifra2)
            for i in range(mensagens):
                puzzle = input()
                objeto_criptografia.set_recebe_puzzle(puzzle)
                print(objeto_criptografia)
            print('')

        except EOFError:
            break

if __name__ == '__main__':
    deciphering_the_encrypted_card()