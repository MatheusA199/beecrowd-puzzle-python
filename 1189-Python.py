opera = str(input())
m=[]
for i in range(12):
    m.append([])

for i in range(12):
    for j in range(12):
        x = float(input())
        m[i].append(x) 

soma = 0
a = 0
b = 1

quantidade = 0
for k in range(1,6):
    for i in range(0,b):
        soma = soma + m[k][i]
        quantidade += 1
    b +=1
b = 5
for k in range(6,11):
    for i in range(0,b):
        soma = soma + m[k][i]
        quantidade += 1
    b -=1
if opera == 'S':
    print('{:.1f}'.format(soma))

if opera == 'M':
    med = soma / quantidade
    print('{:.1f}'.format(med))