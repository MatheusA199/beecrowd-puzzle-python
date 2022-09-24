def the_return_of_radar():
    while True:
        casos = entrada_casos()
        sem_mais_casos = (casos == 0)
        if (sem_mais_casos):
            break
        else:
            for i in range(casos):
                pessoas = entrada_quantidade_pessoas()
                quantidade_par = (pessoas % 2 == 0)
                if (quantidade_par):
                    pedidos =  quantidade_par_pessoas(pessoas)
                    escrever_pedidos(pedidos)
                else:
                    pedidos = quantidade_impar_pessoas(pessoas)
                    escrever_pedidos(pedidos)

def entrada_casos():
    casos = int(input())
    return casos

def entrada_quantidade_pessoas():
    pessoas = int(input())
    return pessoas

def escrever_pedidos(pedidos):
    print(pedidos)

def quantidade_impar_pessoas(pessoas):
    pedidos = (pessoas * 2) - 1
    return pedidos

def quantidade_par_pessoas(pessoas):
    pedidos = (pessoas * 2) - 2
    return pedidos

if (__name__ == '__main__'):
    the_return_of_radar()