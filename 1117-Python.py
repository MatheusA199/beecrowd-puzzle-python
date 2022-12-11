soma=i= 0
while True:
    nota = float(input())
    if 10>=nota >=0:
        soma +=nota
        i +=1
        if i == 2:
            media = soma/2
            print("media =%0.2f" %media)
            break
    else:
        print("nota invalida")