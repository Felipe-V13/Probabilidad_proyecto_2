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

#Acumulada de moneda truco
Ac_geo = []
acum = 0
for x in range(1, lanzamientos+1):
    acum = acum + X_geo_truco[x-1]
    Ac_geo.append(acum)
#Prints de acumulada
cont = 1
print("\nDistribución acumulada del FMP geométrica con moneda truco")
for x in Ac_geo:
    print("F(", cont, ") =", x)
    cont = cont+1

#Graficamos acumulada truco
data = np.arange(0, 12)
y = np.array(Ac_geo)
yn = np.insert(y, 0, 0)

fig, ax = plt.subplots()
ax.set_facecolor('white')           

# Líneas horizontales
ax.hlines(y=yn, xmin=data[:-1], xmax=data[1:],
          color='blue', zorder=1)

#Las líneas puntedas
ax.vlines(x=data[1:-1], ymin=yn[:-1], ymax=yn[1:], color='lightblue',
          linestyle='dashed', zorder=1)

ax.scatter(data[1:-1], y, color='blue', s=18, zorder=2)
ax.scatter(data[1:-1], yn[:-1], color='white', s=18, zorder=2,
           edgecolor='blue')
ax.grid(True)
ax.set_xlim(data[0], data[-1])
ax.set_ylim([-0.01, 1.01])
ax.set_xlabel('X (lanzamientos)')
ax.set_ylabel('F(X)')
ax.set_title('Función de distribución acumulada con moneda truco')

    
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
