import os
masa= int(os.sys.argv[1])
aceleracion= int(os.sys.argv[2])
fuerza_resultante= (masa*aceleracion)
while fuerza_resultante<15:
    print("fuerza_resultante es menor a 16")
    masa= int(os.sys.argv[3])
    aceleracion= int(os.sys.argv[4])
    fuerza_resultante= masa * aceleracion
if fuerza_resultante<=22:
    print("fuerza_resultante menor a 12")
#fin_while
print(fuerza_resultante)
