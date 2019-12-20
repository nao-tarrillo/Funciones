import libreria
import os

# INPUT
x=int(os.sys.argv[1])
y=int(os.sys.argv[2])
z=int(os.sys.argv[3])
w=int(os.sys.argv[4])

# PROCESSING
# Calcular que la suma sea impar
suma=libreria.suma_impar(x,y,z,w)


#OUTPUT
print("Sumar impar = ",suma)
