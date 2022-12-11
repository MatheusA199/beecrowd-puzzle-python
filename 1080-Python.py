x = 0
y = 0
position = 0
lugar = 0
for i in range(1,101):
    x = int(input())
    position += 1
    if y < x:
        y = x
        lugar = position
    else:
        pass
print(y)
print(lugar)