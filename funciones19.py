import libreria
import os


# INPUT
calor_final=int(os.sys.argv[1])
calor_inicial=int(os.sys.argv[2])


# PROCESSING
# Calcular la eficiencia de una maquina
eficiencia=libreria.eficiencia(calor_final,calor_inicial)


#OUTPUT
print("Eficiencia = ",eficiencia)
