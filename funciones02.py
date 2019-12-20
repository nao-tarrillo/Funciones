import libreria
import os

# DECLARAR VARIABLES
velocidad_inicial,aceleracion,tiempo=0,0,0

# INPUT
velocidad_inicial=int(os.sys.argv[1])
aceleracion=int(os.sys.argv[2])
tiempo=int(os.sys.argv[3])

# PROCESSING
# Calcular la velocidad final de un auto
velocidad_final=libreria.pedir_velocidad_final(velocidad_inicial,aceleracion,tiempo)

# OUPUT
print("Velocidad final = ",velocidad_final)
