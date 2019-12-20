import libreria
import os

# DECLARAR VARIABLES
base_menor,base_mayor,altura=0,0,0

# INPUT
base_mayor=int(os.sys.argv[1])
base_menor=int(os.sys.argv[2])
altura=int(os.sys.argv[3])

# PROCESSING
# Encontrar el area de un trapecio
area=libreria.area_trapecio(base_mayor,base_menor,altura)

# OUTPU
print("Area = ", area)
