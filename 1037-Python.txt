x = float(input())

if 75.0000 < x and 100.0000 >= x:
    print("Intervalo (75,100]")
elif 75.0000 >= x and x > 50.0000:
    print("Intervalo (50,75]")
elif 50.0000 >= x and x > 25.0000:
    print("Intervalo (25,50]")
elif 25.0000 >= x and x >= 0.0000:
    print("Intervalo [0,25]")
else:
    print("Fora de intervalo")