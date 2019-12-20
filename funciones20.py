import libreria
import os


# INPUT
constante=int(os.sys.argv[1])
carga=int(os.sys.argv[2])
distancia=int(os.sys.argv[3])


# PROCESSING
# Hallar el campo electrico
campo_electrico=libreria.campo_electrico(constante,carga,distancia)


#OUTPUT
print("Campo electrico = ", campo_electrico)
