import libreria
import os

# INPUT
nombre=str(os.sys.argv[1])
apellidos=str(os.sys.argv[2])
precio=float(os.sys.argv[3])

# PROCESSING
# Entregar boleta electronica
edad_verdadera=libreria.total_precio(precio)

# OUPUT
print("##############################################")
print("###########  FERRETERIA RAMOS  ###############")
print("##############################################")
print("# Cliente : ",nombre,"                       #")
print("# Apellidos : ",apellidos,"                  #")
print("# Precio : ",precio,"                        #")
print("##############################################")
