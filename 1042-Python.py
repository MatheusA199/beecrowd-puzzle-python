x, y, z = input().split()

if int(x) > int(y):
    if int(y) > int(z):
        print(z)
        print(y)
        print(x)
    elif int(x) > int(z):
        print(y)
        print(z)
        print(x)
    elif int(x) < int(z):
        print(y)
        print(x)
        print(z)
else:
    if int(x) > int(z):
        print(z)
        print(x)
        print(y)
    elif int(z) > int(x):
        if int(y) > int(z):
            print(x)
            print(z)
            print(y)
        else:
            print(x)
            print(y)
            print(z)
print("")
print(x)
print(y)
print(z)