class Batmain:
    def __init__(self, vilao):
        self._vilao = vilao

    def __str__(self):
        return 'Y'

def batmain():
    entrada = int(input())
    for i  in range(entrada):
        vilao = input()
        objeto_batmain = Batmain(vilao)
        print(objeto_batmain)

if __name__ == '__main__':
    batmain()