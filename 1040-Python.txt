x = input().split()
N1, N2, N3, N4 = x

media = ((float(N1)*2)+(float(N2)*3)+(float(N3)*4)+(float(N4)*1))/10
print("Media: %0.1f" %media)
if media >= 7:
    print("Aluno aprovado.")
if media<5.0:
    print("Aluno reprovado.")
if 5.0 <= media <= 6.9:
    print('Aluno em exame.')
    exame = float(input())
    print('Nota do exame: {}'.format(exame))
    media2 = (exame + media) / 2
    if media2 >=5:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(media2))
    else:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(media2))