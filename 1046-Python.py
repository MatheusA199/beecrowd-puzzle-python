inicio, fim = list(map(int,input().split()))
if inicio >= fim:
    tempo = (fim+24)-inicio
else:
    tempo = fim - inicio
print("O JOGO DUROU", tempo, "HORA(S)")