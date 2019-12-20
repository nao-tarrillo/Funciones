import libreria
import os

# DECLARAR VARIABLES
pi,radio=0.0,0

# INPUT
pi=float(os.sys.argv[1])
radio=int(os.sys.argv[2])

# PROCESSING
# Calcular el volumen de una esfera
volumen=libreria.volumen_esfera(pi,radio)

# INPUT
print("Volumen = ", int(volumen))
