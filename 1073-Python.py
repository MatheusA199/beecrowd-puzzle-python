N = int(input())

if 5<N<2000:
    for i in range(2,N+1,2):
        square = i**2
        print("{}^2 = {}" .format(i,square))