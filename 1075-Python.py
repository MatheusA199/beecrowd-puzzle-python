N = int(input())

if N<10000:
    for i in range(1,N+1):
        valor = int(input())
        if valor == 0:
            print("NULL")
        else:
            if valor%2 ==0:
                if valor >0:
                    print("EVEN POSITIVE")
                else:
                    print("EVEN NEGATIVE")
            if valor%2 != 0:
                if valor > 0:
                    print("ODD POSITIVE")
                else:
                    print("ODD NEGATIVE")