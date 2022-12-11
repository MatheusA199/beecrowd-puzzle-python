X = int(input())
fibonacci = []
for value in range(X):
  if value<1:
    fibonacci.append(value)
  elif 1==value:
    fibonacci.append(value)
  elif 1<value<=3:
    fibonacci.append(value-1)
  elif value>3:
    num = fibonacci[-1]+fibonacci[-2]
    fibonacci.append(num)

print(*fibonacci)
  