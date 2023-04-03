import random

# Largo/longitud de la secuencia
seq_len = 10

# Secuencia de los lanzamientos
seq = []
for i in range(seq_len):
    moneda_fich = random.choice(['escudo', 'corona'])
    seq.append(moneda_fich)

# resultado
print(seq)
