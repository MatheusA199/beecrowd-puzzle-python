X = int(input())
while True:
  Z = int(input())
  if Z <=X:
    pass
  else:
    break
soma = 0
num = []
for value in range(X,Z+1):
  soma +=value
  num.append(value)
  if soma >Z:
    break
print(len(num))