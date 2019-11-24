import os
direccion= os.sys.argv[1]
nro_letras = 0
for a in direccion:
    print(a)
    nro_letras +=1
    if nro_letras ==9:
        print("acertado")
#fin_for
print("La direccion tiene:",nro_letras, "LETRAS")
