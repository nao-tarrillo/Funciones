import libreria
import os

# DECLARAR VARIABLES
densidad_liquido,gravedad,altura=0,0,0

# INPUT
densidad_liquido=int(os.sys.argv[1])
gravedad=int(os.sys.argv[2])
altura=int(os.sys.argv[3])

# PROCESSING
# Calcular la presion?
presion=libreria.presion(densidad_liquido,gravedad,altura)

# OUTPUT
print("Presion = ", int(presion))
