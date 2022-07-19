x = input().split()
a, b = x
a, b, = int(a), int(b)

if (b > 0):
	quociente = a//b
	resto = a % b
else:
	quociente = (a // abs(b))*(-1)
	resto = a % abs(b)
print(f'{quociente} {resto}')
