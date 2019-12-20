import libreria
import os

# DECLARAR VARIABLES
divisor,cociente,residuo=0,0,0

# INPUT
divisor=int(os.sys.argv[1])
cociente=int(os.sys.argv[1])
residuo=int(os.sys.argv[1])

# PROCESSING
# Calcular el dividendo
dividendo=libreria.dividendo(divisor,cociente,residuo)

# OUTPUT
print("Dividendo = ",dividendo)
