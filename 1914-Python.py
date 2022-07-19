n = int(input())

for i in range(n):
 	nomes_escolhas = input().split()
 	numeros = input().split()
 	nomes = [] 

 	if (nomes_escolhas[1] == 'PAR'):
 		jogador_par = nomes_escolhas[0]
 		jogador_impar = nomes_escolhas[2]
 	else:
 		jogador_impar = nomes_escolhas[0]
 		jogador_par = nomes_escolhas[2] 		

 	soma = 0
 	for i in numeros:
 		soma += int(i)

 	par = (soma%2 == 0)
 	if (par):
 		print(jogador_par)
 	else:
 		print(jogador_impar)
