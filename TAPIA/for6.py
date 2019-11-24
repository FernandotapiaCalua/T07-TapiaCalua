import os
cad = os.sys.argv[1]
nro_letras = 0
for letra in cad:
    print(letra)
    nro_letras +=1
    if nro_letras == 15:
        print("muy mal")
#fin_for
print("la cadena tiene:",nro_letras)
