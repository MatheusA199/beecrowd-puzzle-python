entrada = input().split()

def escrever_vit1():
	print('Jogador 1 ganha!')

def escrever_vit2():
	print('Jogador 2 ganha!')

escolha_jogador1, jogada_player1, jogada_player2, trapaca, acusacao = entrada

soma_jogadas = int(jogada_player1) + int(jogada_player2)
par = (soma_jogadas % 2 == 0)

if (trapaca == '1'):
	if (acusacao == '0'):
		escrever_vit1()

	else (acusacao == '1'):
		escrever_vit2()

elif(trapaca == '0'):
	if (par):
		if (escolha_jogador1 == '1'):
			escrever_vit1()
		else:
			escrever_vit2()

	elif (not par):
		if (escolha_jogador1 == '0'):
			escrever_vit1()
		else:
			escrever_vit2()
