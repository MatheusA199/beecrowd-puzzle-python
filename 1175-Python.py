list = []
for i in range(20):
    list.append(int(input()))
list.reverse()
i = 0
for value in list:
    print(f'N[{i}] = {value}')
    i +=1