import os
cad = os.sys.argv[1]
cad2 = os.sys.argv[2]
cad3 = os.sys.argv[3]
nro_letras = 0
for letra in cad:
    print(letra)
    nro_letras +=1
    if nro_letras == 22:
        print("y ya es muy tarde")
for letra in cad2:
    print(letra)
    nro_letras +=1
    if nro_letras == 22:
        print("y ya es muy tarde")
for letra in cad3:
    print(letra)
    nro_letras +=1
    if nro_letras == 22:
        print("y ya es muy tarde")
#fin_for
print("la cadena tiene:",nro_letras)
