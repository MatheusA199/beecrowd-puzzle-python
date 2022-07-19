n = int(input())
for i in range(1, n+1):
	x = input().split()
	sheldon, raj = x

	a = 'tesoura'
	b = 'papel'
	c = 'pedra'
	d = 'lagarto'
	e = 'Spock'

	vit_sheldon = {
		'sheldon_1' : a+b,
		'sheldon_2' : b+c,
		'sheldon_3' : c+d,
		'sheldon_4' : d+e,
		'sheldon_5' : e+a,
		'sheldon_6' : a+d,
		'sheldon_7' : d+b,
		'sheldon_8' : b+e,
		'sheldon_9' : e+c,
		'sheldon_10' : c+a,
	}

	empate = {
		'empate_1' : a+a,
		'empate_2' : b+b,
		'empate_3' : c+c,
		'empate_4' : d+d,
		'empate_5' : e+e,
	}
	

	for key, value in vit_sheldon.items():
		if  (sheldon+raj == value):
			print(f'Caso #{i}: Bazinga!')
		elif (raj+sheldon == value):
			print(f'Caso #{i}: Raj trapaceou!')

	for key, value in empate.items():
		if (sheldon+raj) == value:
			print(f'Caso #{i}: De novo!')
		

