n = int(input())

for i in range(n):

	list = input().split()

	yes = list[0] =='Thor'
	
	if (yes):
		print('Y')
	else:
		print('N')