import libreria
import os


# INPUT
resisitividad_electrica=int(os.sys.argv[1])
longitud=int(os.sys.argv[2])
area=int(os.sys.argv[3])


# PROCESSING
# Calcular la resistencia electrica mediante la ley de paulet
resistencia=libreria.ley_poulet(resisitividad_electrica,longitud,area)


#OUTPUT
print("Resistencia electrica = ",resistencia)
