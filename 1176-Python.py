fibonacci = [0,1] 
testes = int(input())
for i in range(testes):
    posicao = int(input())
    if posicao <=1:
        print(f'Fib({posicao}) = {fibonacci[posicao]}')
    else:
        for value in range(2,(posicao+1)):
            fibonacci.append(fibonacci[-2]+fibonacci[-1])
        print(f'Fib({posicao}) = {fibonacci[posicao]}')