import random

# Definir la probabilidad de obtener escudo
prob_escudo = 0.7


# Generar una secuencia de 10 lanzamientos
secuencia = []
for i in range(10):
    lanzamiento = random.choices(['escudo', 'corona'], weights=[prob_escudo, 1-prob_escudo])[0]
    secuencia.append(lanzamiento)

# Imprimir la secuencia generada
print(secuencia)
