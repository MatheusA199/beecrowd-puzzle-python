coelho = []
rato = []
sapo = []
c = 0
r = 0
s = 0
x= []
i = 0
N = int(input())
while i < N:
    x = input().split()
    i += 1
    if x[1] == "C":
        coelho.append(x[0])
        c += 1
    elif x[1] == "R":
        rato.append(x[0])
        r += 1
    elif x[1] == "S":
        sapo.append(x[0])
        s += 1
i = 0
j = 0
g = 0
somaC = 0
somaR = 0
somaS = 0
while i < c:
    somaC += int(coelho[i])
    i += 1
while j < r:
    somaR += int(rato[j])
    j += 1
while g < s:
    somaS += int(sapo[g])
    g += 1

total = somaC+somaR+somaS
porcC = (somaC*100)/total
porcR = (somaR*100)/total
porcS = (somaS*100)/total
print("Total: {} cobaias" .format(total))
print("Total de coelhos: {}" .format(somaC))
print("Total de ratos: {}" .format(somaR))
print("Total de sapos: {}" .format(somaS))
print("Percentual de coelhos: %.2f" %porcC,"%")
print("Percentual de ratos: %.2f" %porcR,"%")
print("Percentual de sapos: %.2f" %porcS,"%")