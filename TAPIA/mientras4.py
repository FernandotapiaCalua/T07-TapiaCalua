import os
masa= int(os.sys.argv[1])
velocidad= int(os.sys.argv[2])
cantidad_de_movimiento= masa*velocidad
while cantidad_de_movimiento<50:
    print("la canitdad de movimiento es mayor")
if cantidad_de_movimiento<12:
    print("la canitdad de movimiento es menor")
#fin_while
print(cantidad_de_movimiento)
