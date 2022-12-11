import math
class FibonacciFast:
    def __init__(self,natural):
        self._natural = natural
        
    @property    
    def formula_binet(self):
        valor1 = ((1+ math.sqrt(5))/2)
        parte_soma = valor1 ** self._natural

        valor2 = ((1-math.sqrt(5))/2)
        parte_subtracao = valor2 ** self._natural

        formula = (parte_soma - parte_subtracao) / (math.sqrt(5))
        return formula

    def __str__(self):
        formula = self.formula_binet
        return f'{formula:.1f}'

def fast_fibonacci(Fibonacci_fast):
    natural = int(input())
    valor = FibonacciFast(natural)
    print(valor)

if (__name__ == '__main__'):
    fast_fibonacci(FibonacciFast)