import os
cantidad_de_calor=  int(os.sys.argv[1])
trabajo=  int(os.sys.argv[2])
variacion_de_energia_interna= cantidad_de_calor * trabajo
while variacion_de_energia_interna>35:
    print("la cantidad es mayor")
    cantidad_de_calor=  int(os.sys.argv[3])
    trabajo=  int(os.sys.argv[4])
    variacion_de_energia_interna= cantidad_de_calor * trabajo
if variacion_de_energia_interna<30:
    print("la cantidad es menor")
#fin_mientras
