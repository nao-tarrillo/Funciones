import libreria
import os

# DECLARAR VARIABLES
masa,longitud,tiempo=0,0,0

# INPUT
masa=int(os.sys.argv[1])
longitud=int(os.sys.argv[2])
tiempo=int(os.sys.argv[3])

# PROCESIING
# Calcular la fuerza emitida por un ser humano?
fuerza=libreria.fuerza(masa,longitud,tiempo)

# OUTPUT
print("Fuerza = ", int(fuerza))
