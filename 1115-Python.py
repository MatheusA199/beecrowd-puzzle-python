while True:
    X,Y = input().split()
    X = int(X)
    Y = int(Y)
    if X ==0 or Y == 0:
        break
    else:
        if X > 0:
            if Y > 0:
                print("primeiro")
            else:
                print("quarto")
        else:
            if Y < 0:
                print("terceiro")
            else:
                print("segundo")

