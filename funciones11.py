import libreria
import os

# DECLARAR VARIABLES
nombre1,nombre2,apellido1,apellido2="","","",""


# INPUT
nombre1=os.sys.argv[1]
nombre2=os.sys.argv[2]
apellido1=os.sys.argv[3]
apellido2=os.sys.argv[4]

# PROCESSING
# Averiguar el nombre del presidente del peru
nombre_completo=libreria.nombre_completo(nombre1,nombre2,apellido1,apellido2)

# OUTPUT
print("Nombre Del Presidente = ", nombre_completo)
