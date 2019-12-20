import libreria
import os

# INPUT
nombre=str(os.sys.argv[1])
cantidad_arroz=int(os.sys.argv[2])
cantidad_azucar=int(os.sys.argv[3])
cantidad_fideo=int(os.sys.argv[4])
precio_arroz=float(os.sys.argv[5])
precio_azucar=float(os.sys.argv[6])
precio_fideo=float(os.sys.argv[7])

# PROCESSING
# Entregar boleta de venta
total=libreria.boleta(cantidad_arroz,cantidad_azucar,cantidad_fideo,precio_arroz,precio_azucar,precio_fideo)

#OUPUT
print("######################################################")
print("#########       BODEGA FLORES          ###############")
print("######################################################")
print("# Cliente : ", nombre,"                              #")
print("# Arroz : ",cantidad_azucar,"#   Precio :",precio_arroz," #")
print("# Azucar : ",cantidad_azucar,"# Precio : ",precio_azucar,"#")
print("# Fideo : ",cantidad_fideo, "# Precio : ", precio_fideo," #")
print("######################################################")
print("# Total : ", total,"                                 #")
print("######################################################")
