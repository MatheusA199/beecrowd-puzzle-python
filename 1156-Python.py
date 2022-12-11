while True:
  x = int(input())
  soma = 0
  if x ==0:
    break
  if x %2 !=0:
    x +=1
  for i in range(x, x+9,2):
    soma +=i
  print(soma)