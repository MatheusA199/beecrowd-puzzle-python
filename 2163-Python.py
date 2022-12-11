class SabreDeLuz:
    def __init__(self,linha, coluna,matriz) -> None:
        self._linha = linha
        self._coluna = coluna
        self._matriz = matriz
        
    def verificacao(self):
        for i in range(1,self._linha - 1):

            for j in range(1,self._coluna - 1):

                if self._matriz[i][j] == 42:
                    
                    if (self._matriz[i][j-1] != 7):
                        pass

                    elif (self._matriz[i][j+1] != 7):
                        pass

                    elif (self._matriz[i+1][j-1] != 7):
                        pass
                    
                    elif (self._matriz[i+1][j] != 7):
                        pass

                    elif(self._matriz[i+1][j+1] != 7):
                        pass
                    
                    elif (self._matriz[i-1][j-1] != 7):
                        pass

                    elif (self._matriz[i-1][j] != 7):
                        pass

                    elif (self._matriz[i-1][j+1] != 7):
                        pass

                    else:
                        x = i
                        y = j
                        return x,y

    def __str__(self) -> str:
        try:
            x,y = self.verificacao()
            return (f'{x+1} {y+1}')
        except:
            return (f'0 0')


def the_force_awakens(SabreDeLuz):
    linha, coluna = map(int,input().split(' '))
    matriz = []

    for i in range(linha):
        matriz.append(list(map(int, input().split(' '))))

    objeto = SabreDeLuz(linha, coluna,matriz)
    print(objeto)
        
if (__name__ == '__main__'):
    the_force_awakens(SabreDeLuz)