maior = str(input())
medio = str(input())
pequeno = str(input())

if maior == "vertebrado":
    if medio == "ave":
        if pequeno == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if pequeno == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if medio == "inseto":
        if pequeno == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if pequeno == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")