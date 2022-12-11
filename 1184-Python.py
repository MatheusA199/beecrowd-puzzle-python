opera = str(input())
m=[]
for i in range(12):
    m.append([])

for i in range(12):
    for j in range(12):
        x = float(input())
        m[i].append(x) 

soma = 0
c = 0
quantidade = 0
for k in range(0,12):
    for i in range(0,c):
        soma = soma + m[k][i]
        quantidade += 1
    c +=1

if opera == 'S':
    print(quantidade)
    print('{:.1f}'.format(soma))

if opera == 'M':
    med = soma / quantidade
    print('{:.1f}'.format(med))