vitInter,vitGremio,empates,grenais,a=0,0,0,0,1
while (a==1):
    inter,gremio = input().split()
    grenais += 1
    if a==1:
        if inter >gremio:
            vitInter +=1
        elif inter<gremio:
            vitGremio +=1
        else:
            empates += 1
    a = int(input("Novo grenal (1-sim 2-nao)\n"))
    if a==2:
        break
print("{} grenais" .format(grenais))
print("Inter:{}" .format(vitInter))
print("Gremio:{}" .format(vitGremio))
print("Empates:{}" .format(empates))
if vitGremio > vitInter:
    print("Gremio venceu mais")
elif vitGremio == vitInter:
    print("N�o houve vencedor")
else:
    print("Inter venceu mais")