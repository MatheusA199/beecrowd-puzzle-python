x = 0
while True:
    valores = [int(x) for x in input().split()]
    if valores[x] == valores[x+1]:
        break
    else:
        if valores[x] > valores[x+1]:
            print("Decrescente")
        else:
            print("Crescente")
