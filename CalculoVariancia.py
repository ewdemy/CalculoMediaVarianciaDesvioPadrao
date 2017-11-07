from math import sqrt

vet1 = []
vet2 = []
media = 0.00
soma = 0.00
soma2 = 0.00
media2 = 0.00

print ("------------ CÁLCULO MÉDIA, DESVIO PADRÃO E VARIÂNCIA -------------")
print (" ")
entrada = int(input("Quantidade de entradas: "))

for i in range(entrada):
    print("Entrada ",i+1,":")
    vet1.append(float(input()))

for i in vet1:
    soma += i

media = (soma / entrada)

for i in vet1:
    vet2.append((i - media)**2)

for i in vet2:
    soma2 += i

media2 = (soma2 / (entrada -1))
media3 = (soma2 / entrada)

desvioA = sqrt(media2)
desvioP = sqrt(media3)

print ("Média: %.2f"%media)
print ("Desvio Padrão Amostral: %.2f"%desvioA)
print ("Desvio Padrão Populacional: %.2f"%desvioP)
print ("Variancia Amostral: %.2f"%media2)
print ("Variancia Populacional: %.2f"%media3)


