valor = float(input())
if valor <=400.00:
    taxa = "15 %"
    reajuste = 400.00*0.15
    salario = reajuste + valor
elif 800.00 >= valor:
    taxa = "12 %"
    reajuste = valor * 0.12
    salario = reajuste + valor
elif 1200.00 >= valor:
    taxa = "10 %"
    reajuste = valor * 0.10
    salario = reajuste + valor
elif valor <= 2000.00:
    taxa = "7 %"
    reajuste = valor * 0.07
    salario = reajuste + valor
elif valor > 2000:
    taxa = "4 %"
    reajuste = valor * 0.04
    salario = reajuste + valor

print("Novo salario: %0.2f" %salario)
print("Reajuste ganho: %0.2f" %reajuste)
print("Em percentual:", taxa )