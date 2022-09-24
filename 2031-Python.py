rodadas = int(input())

vitoria = {
	'pedra_tesoura': 'pedra' + 'ataque',
	'papel_pedra': 'papel' + 'pedra',
	'tesoura_papel': 'ataque' + 'papel',}

empate_situacao = {
	'papelpapel': 'Ambos venceram',
	'pedrapedra': 'Sem ganhador',
	'ataqueataque': 'Aniquilacao mutua',
}

for i in range(rodadas):
	jogada_jogador_1 = str(input())
	jogada_jogador_2 = str(input())

	verificacao_1 = jogada_jogador_1 + jogada_jogador_2
	verificacao_2 = jogada_jogador_2 + jogada_jogador_1
	empate = verificacao_2 == verificacao_1
	if (empate):
		for key, value in empate_situacao.items():
			if (verificacao_1 == key):
				print(value)

	else:
		for key, value in vitoria.items():
			if (verificacao_1 == value): 
				print(f'Jogador 1 venceu')
			elif(verificacao_2 == value):
				print(f'Jogador 2 venceu')


