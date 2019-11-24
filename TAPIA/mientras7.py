import os
frecuencia=  int(os.sys.argv[1])
periodo= 1/frecuencia
while periodo>=0.25:
    print("el periodo es correcto")
    frecuencia=  int(os.sys.argv[2])
    periodo= 1/frecuencia
if periodo==0.10:
    print("el periodo es incorrecto")
#fin_mientras
print(periodo)

