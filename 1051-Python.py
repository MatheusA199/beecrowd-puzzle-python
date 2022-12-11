renda = float(input())

renda = renda - 2000.00
taxa = 0
if (renda - 1000)>=0:
    taxa = 1000*0.08
    renda = renda-1000
    if (renda-1500)>= 0:
        taxa += 1500*0.18
        renda = renda-1500
        if renda > 0:
            taxa += renda * 0.28
    else:
        taxa += renda*0.18
else:
    taxa += renda*0.08
if renda <0:
    print("Isento")
else:
    print("R$ %.2f" %taxa)