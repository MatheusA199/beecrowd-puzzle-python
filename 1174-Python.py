list = []
for i in range(100):
    list.append(float(input()))

i = 0
for value in list:
    if value <=10:
        print('A[{}] = {:0.1f}' .format(i, value))
    i +=1