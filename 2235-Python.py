class ViagemNoTempo:
    def __init__(self,credito1, credito2, credito3) -> None:
        self._credito1 = credito1
        self._credito2 = credito2
        self._credito3 = credito3
    def validacoes(self):
        var1 = self._credito1 == self._credito2
        var2 = self._credito1 == self._credito3
        var3 = self._credito2 == self._credito3
        var4 = (self._credito1 + self._credito2 - self._credito3) == 0
        var5 = (self._credito1 + self._credito3 - self._credito2) == 0
        var6 = (self._credito2 + self._credito3 - self._credito1) == 0
        if (var1) or (var2) or (var3) or (var4) or (var5) or (var6):
            return 'S'
        
        else:
            return 'N'
    def __str__(self) -> str:
        return self.validacoes()

def walking_in_time(ViagemNoTempo):   
    credito1, credito2, credito3 = map(int, input().split(' '))

    objeto = ViagemNoTempo(credito1, credito2, credito3)
    print(objeto)

if (__name__ == '__main__'):
    walking_in_time(ViagemNoTempo)