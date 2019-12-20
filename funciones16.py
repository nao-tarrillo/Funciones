import libreria
import os

# INPUT
longitud=int(os.sys.argv[1])
tiempo=int(os.sys.argv[2])
temperatura=int(os.sys.argv[3])


# PROCESSING
# Hallar el calor especifico que libera un cuerpo
calor_especifico=libreria.calor_especifico(longitud,tiempo,temperatura)


#OUTPUT
print("Calor especifico = ", int(calor_especifico))
