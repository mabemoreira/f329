from decimal import *

getcontext().prec = 6
n = int(input("Quantos numeros vc vai passar? "))
n_video = int(input("Qual o numero do video? "))
anterior = 0
lista_periodos = []

for i in range(n):
    tempo_atual = float(input(f"insira o tempo do pico de numero {i+1}: "))
    periodo_atual = Decimal(Decimal(tempo_atual) - Decimal(anterior))
    anterior = tempo_atual
    lista_periodos.append(periodo_atual)


print(f"Video {n_video}:")
for i in range(len(lista_periodos)):
    print(f"{i+1} - {lista_periodos[i]}")

lista_periodos.pop(0)

media = Decimal(Decimal(sum(lista_periodos))/len(lista_periodos))
freq_ao_quadrado = 1/(media ** 2)
print(f"frequencia ao quadrado: {freq_ao_quadrado}")
print(f"media: {media}")
