lados = input().split()
a, b, c, d = lados
a = int(a)
b = int(b)
c = int(c)
d = int(d)

def sim():
	print('S')
# a b c
verificacao_1 = abs(a-c) < b < abs(a+c)

# a d b
verificacao_2 = abs(a-d) < b < abs(a+d)

# a c d
verificacao_3 = abs(a-c) < d < abs(a+c)

#b c d
verificacao_4 = abs(b-c) < d < abs(b+c)

if (verificacao_1):
	sim()
elif (verificacao_2):
	sim()
elif (verificacao_3):
	sim()
elif (verificacao_4):
	sim()
else:
	print('N')