import os
nombre = os.sys.argv[1]
nro_letras = 0
for letra in nombre:
    print(letra)
    nro_letras +=1
    if nro_letras == 20:
        print("bien")
#fin_for
print("el nombre tiene:",nro_letras)
