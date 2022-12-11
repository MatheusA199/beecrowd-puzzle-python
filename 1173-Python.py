n = int(input())
for i in range(10):
  if i ==0:
    print('N[{}] = {}' .format(i,n))
  else:
    n = n*2
    print('N[{}] = {}' .format(i,n))