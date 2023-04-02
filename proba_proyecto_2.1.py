
import random

# Definir variables para contar las caras y las cruces
num_caras = 0
num_cruces = 0

# Lanzar la moneda 10 veces y registrar los resultados
i = 0
while i < 10:
    resultado = random.choice(['cara', 'cruz'])
    if resultado == 'cara':
        num_caras += 1
    else:
        num_cruces += 1
    i += 1

#frecuencia
# de
# las salidas

frecuencia_caras = num_caras / 10.0
frecuencia_cruces = num_cruces / 10.0

# Imprimir los resultados
print("caras: ", num_caras)
print("cruces ", num_cruces)
