import libreria
import os

# DECLARAR VARIABLES
nota01,nota02,nota03,nota04=0,0,0,0

# INPUT
nota01=int(os.sys.argv[1])
nota02=int(os.sys.argv[2])
nota03=int(os.sys.argv[3])
nota04=int(os.sys.argv[4])

# PROCESSING
# Calcular el promedio final del curso
promedio_final=libreria.promedio(nota01,nota02,nota03,nota04)

# OUPUT
print("Promedio final = ",promedio_final)
