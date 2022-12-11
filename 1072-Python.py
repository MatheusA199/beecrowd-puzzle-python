total = int(input())
dentro = 0
fora = 0
for i in range(total):
    valor = int(input())
    if 20>= valor >=10:
        dentro +=1
    else:
        fora +=1
print("{} in" .format(dentro))
print("{} out" .format(fora))