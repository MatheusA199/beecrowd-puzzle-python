X = int(input())

if X%2 == 0:
    for i in range(X+1,X+12,2):
        print(i)
else:
    for i in range(X,X+12,2):
        print(i)
