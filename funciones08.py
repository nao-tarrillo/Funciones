import libreria
import os

# DECLARAR VARIABLES
masa,velocidad,radio=0,0,0

# INPUT
masa=int(os.sys.argv[1])
velocidad=int(os.sys.argv[1])
radio=int(os.sys.argv[1])

# PROCESSING
# Calcular la fuerza centripeta generado por un cuerpo en una curva
fuerza_centripeta=libreria.fuerza_centripeta(masa,velocidad,radio)

# OUTPUT
print("Fuerza centripeta = ", int(fuerza_centripeta))
