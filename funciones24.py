import libreria
import os


# INPUT
n1=int(os.sys.argv[1])
n2=int(os.sys.argv[2])
n3=int(os.sys.argv[3])
n4=int(os.sys.argv[4])
n5=int(os.sys.argv[5])
n6=int(os.sys.argv[6])


# PROCESSING
# Calcular la siguiente operacion
opercion=libreria.operacion(n1,n2,n3,n4,n5,n6)


#OUTPUT
print("Operacion = ",opercion)
