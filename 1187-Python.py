opera = str(input())
m=[]
for i in range(12):
    m.append([])

for i in range(12):
    for j in range(12):
        x = float(input())
        m[i].append(x) 

soma = 0
a = 1
b = 11

quantidade = 0
for k in range(0,5):
    for i in range(a,b):
        soma = soma + m[k][i]
        quantidade += 1
    b -=1
    a +=1
if opera == 'S':
    print('{:.1f}'.format(soma))

if opera == 'M':
    med = soma / quantidade
    print('{:.1f}'.format(med))