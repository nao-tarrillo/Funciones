import libreria
import os
# DECLARAR VARIABLES
velocidad,tiempo=0,0

# INPUT
# Calcular la distancia que recorre un auto?
velocidad=int(os.sys.argv[1])
tiempo=int(os.sys.argv[2])

# PROCESSING
distancia=libreria.distancia(velocidad,tiempo)


# OUTPUT
print("Distancia = ",int(distancia))



