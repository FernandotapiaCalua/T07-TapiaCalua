import os
caracteres = os.sys.argv[1]
nro_vocales = 0
for vocal in caracteres:
    print(vocal)
    nro_vocales +=1
    if nro_vocales == 5:
        print("ok")
#fin_for
print("las vocales son:",nro_vocales, "vocales")
