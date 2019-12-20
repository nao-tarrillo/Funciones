import libreria
import os

# DECLARAR VARIABLES
velocidad_inicial,tiempo,gravedad=0,0,0

# INPUT
velocidad_inicial=int(os.sys.argv[1])
tiempo=int(os.sys.argv[2])
gravedad=int(os.sys.argv[3])

# PROCESSING
# Calcular la altura que alcanza un cuerpo al ser lanzado desde el piso?
altura=libreria.altura(velocidad_inicial,tiempo,gravedad)

# OUTPUT
print("Altura = ", int(altura))
