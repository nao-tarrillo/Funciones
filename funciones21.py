import libreria
import os


# INPUT
constante=int(os.sys.argv[1])
carga01=int(os.sys.argv[2])
carga02=int(os.sys.argv[3])
distancia=int(os.sys.argv[4])


# PROCESSING
# Calcular la fuerza electrica realizada por una carga
fuerza_electrica=libreria.fuerza_electrica(constante,carga01,carga02,distancia)


#OUTPUT
print("Fuerza electrica = ",fuerza_electrica)
