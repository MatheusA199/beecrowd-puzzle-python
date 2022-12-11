lados = input().split()

A, B, C = sorted(lados)
A = float(A)
B = float(B)
C = float(C)

if A >= B and A >=C:
    if B>= C:
        pass
    else:
        B, C = C, B
else:
    if B >= C:
        A, B, C = B, C, A
    else:
        A, B, C = C, B, A

if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if A ** 2 == B ** 2 + C ** 2:
        print("TRIANGULO RETANGULO")
    if A ** 2 > B ** 2 + C ** 2:
        print("TRIANGULO OBTUSANGULO")
    if A ** 2 < B ** 2 + C ** 2:
        print("TRIANGULO ACUTANGULO")
    if A == C and B == C:
        print("TRIANGULO EQUILATERO")
    if A == B != C or C == B != A or A == C != B:
        print("TRIANGULO ISOSCELES")