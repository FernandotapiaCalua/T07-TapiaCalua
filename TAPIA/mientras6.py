import os
masa=  int(os.sys.argv[1])
calor_latente=  int(os.sys.argv[2])
cantidad_de_calor= masa*calor_latente
while cantidad_de_calor>55:
    print("la cantidad de calor es muy alta")
    masa=  int(os.sys.argv[4])
    calor_latente=  int(os.sys.argv[4])
    cantidad_de_calor= masa * calor_latente
if cantidad_de_calor<30:
    print("la cantidad de calor es aceptable")
#fin_while
