import libreria
import os

# INPUT
presion=int(os.sys.argv[1])
volumen=int(os.sys.argv[2])
mol=int(os.sys.argv[3])
constante=int(os.sys.argv[4])

# PROCESSING
# Calcular la temperatura de un cuerpo
temperatura=libreria.temperatura(presion,volumen,mol,constante)

# OUTPUT
print("Temperatura = ", int(temperatura),"°")
