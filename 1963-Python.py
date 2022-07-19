valores = input().split()
valor_1, valor_2 = valores

valor_1 = float(valor_1)
valor_2 = float(valor_2)

porcentagem = (((valor_2/valor_1)*100)-100)

print(f"{porcentagem:.2f}%")