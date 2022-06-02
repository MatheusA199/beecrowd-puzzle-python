a = input().split()
b = input().split()
codigo1, quantidade1, preco1 = a
codigo2, quantidade2, preco2 = b

pagar = (int(quantidade1)*float(preco1))+(int(quantidade2)*float(preco2))
print("VALOR A PAGAR: R$ %0.2f" %pagar)