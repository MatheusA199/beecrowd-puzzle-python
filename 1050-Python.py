#Por meio de um dicionário.
ddd = int(input())
estado = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte",
}
print( estado.get(ddd, "DDD nao cadastrado"))
#Colocar o get para ter uma resposta caso não tenha o input.