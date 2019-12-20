import libreria
import os

# INPUT
longitud_inicial=float(os.sys.argv[1])
alfa=float(os.sys.argv[2])
variacion_temperatura=float(os.sys.argv[3])


# PROCESSING
# Calcular la variacion de la longitud de un fierro al ser dilata
variacion_longitud=libreria.variacion_longitud(longitud_inicial,alfa,variacion_temperatura)


#OUTPUT
print("Variacion de la longitud = ", int(variacion_longitud))
