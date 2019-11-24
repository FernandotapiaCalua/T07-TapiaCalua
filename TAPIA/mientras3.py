import os
velocidad= int(os.sys.argv[1])
tiempo= int(os.sys.argv[2])
distancia= velocidad*tiempo
while distancia >=15:
    print("la distancia no es considerable")
    velocidad= int(os.sys.argv[3])
    tiempo= int(os.sys.argv[4])
    distancia= velocidad*tiempo
if distancia==10:
    print("la distacia es considerable")
#fin_while
