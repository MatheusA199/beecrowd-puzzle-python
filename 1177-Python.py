t = int(input())
i = 0
for value in range(1000):
    if i < t:
        print(f'N[{value}] = {i}')
        i +=1
    else:
        i = 0
        print(f'N[{value}] = {i}')
        i +=1