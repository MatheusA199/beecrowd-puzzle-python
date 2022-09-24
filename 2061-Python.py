entrada = input().split()

aba_inicial, movimentos = entrada
aba_inicial = int(aba_inicial)

for i in range(int(movimentos)):
	ato = str(input())
	if (ato == 'fechou'):
		aba_inicial +=1
	if (ato == 'clicou'):
		aba_inicial -= 1

print(aba_inicial)
