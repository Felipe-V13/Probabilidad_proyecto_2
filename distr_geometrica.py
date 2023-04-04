import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
    
def fmp_geometrica(p, x):
    res = p*((1-p)**(x-1))
    return res

def media_geometrica(p):
    res = 1/p
    return res

def varianza_geometrica(p):
    res = (1-p)/p**2
    return res
    
X_geo_ideal = []
X_geo_truco = []
lanzamientos = 10

#MONEDA IDEAL
p = 0.5
#Recordar que no existe X = 0
for x in range(1, lanzamientos+1):
    X_geo_ideal.append(fmp_geometrica(p, x))
#Prints de moneda ideal    
cont=1
print("\nFPM moneda ideal distribución geométrica")
for x in X_geo_ideal:
    print("P( X =", cont, ") = f(", cont, ") =", x)
    cont = cont+1
print("Media: ", media_geometrica(p))
print("Varianza: ", varianza_geometrica(p))  
print("Desviación estándar: ", sqrt(varianza_geometrica(p)))    

#MONEDA TRUCO
p = 0.3
#Recordar que no existe X = 0
for x in range(1, lanzamientos+1):
    X_geo_truco.append(fmp_geometrica(p, x))    
#Prints de moneda truco
cont = 1
print("\nFPM moneda truco distribución geométrica")
for x in X_geo_truco:
    print("P( X =", cont, ") = f(", cont, ") =", x)
    cont = cont+1
print("Media: ", media_geometrica(p))
print("Varianza: ", varianza_geometrica(p))  
print("Desviación estándar: ", sqrt(varianza_geometrica(p)))  

# Graficamos para moneda ideal
ejex = np.arange(1, lanzamientos+1)
fig = plt.figure()
host = fig.add_subplot()
par = host.twiny()

host.bar(ejex, X_geo_ideal, width=0.04)   #puntos de gráfico
par.scatter(ejex, X_geo_ideal)            #barras de gráfico
par.axes.get_xaxis().set_ticks([])
host.locator_params(axis="x", nbins=lanzamientos)
host.set_title("fmp distribución geométrica para moneda ideal")
host.set_xlabel("x (lanzamiento)")
host.set_ylabel("f(x)")

# Graficamos para moneda truco
ejex = np.arange(1, lanzamientos+1)
fig = plt.figure()
host = fig.add_subplot()
par = host.twiny()

host.bar(ejex, X_geo_truco, width=0.04)
par.scatter(ejex, X_geo_truco)
par.axes.get_xaxis().set_ticks([])
host.locator_params(axis="x", nbins=lanzamientos)
host.set_title("fmp distribución geométrica para moneda truco")
host.set_xlabel("x (lanzamiento)")
host.set_ylabel("f(x)")
