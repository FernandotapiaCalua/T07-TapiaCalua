import os
digitos = os.sys.argv[1]
nro_numeros = 0
for numero in digitos:
    print(numero)
    nro_numeros +=1
    if nro_numeros == 8:
        print("muy bien")
#fin_for
print("la cantidad de digitos es:",nro_numeros, "digitos")
