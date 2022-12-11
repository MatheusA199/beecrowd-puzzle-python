age = int(input())

ano = age//365
age = age%365

mes = age//30
age = age%30

dia = age

print(ano, 'ano(s)')
print(mes, 'mes(es)')
print(dia, 'dia(s)')
