import os
fuerza= int(os.sys.argv[1])
area= int(os.sys.argv[2])
presion= fuerza/area
while presion>=20:
    print("la presion es positiva")
    fuerza=int(os.sys.argv[3])
    area= int(os.sys.argv[4])
    presion= fuerza / area
if presion<6:
    print("la presion es debil")
#fin_while
