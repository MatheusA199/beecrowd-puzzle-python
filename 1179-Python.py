par = []
impar = []
for i in range(15):
    valor = int(input())
    if(valor % 2 == 0):
        par.append(valor)
    else:
        impar.append(valor)
        
    if (len(par)==5):
        for i in range(5):
            print(f'par[{i}] = {par[i]}')
        par = []
    if len(impar)==5:
        for i in range(5):
            print(f'impar[{i}] = {impar[i]}')
        impar = []
if (len(impar)> 0):
    i = 0
    for value in impar:
        print(f"impar[{i}] = {value}")
        i +=1

if(len(par)>0):
    i = 0
    for value in par:
        print(f"par[{i}] = {value}")
        i +=1