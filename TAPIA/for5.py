import os
tipos_de_lapiz = os.sys.argv[1]
tipos_de_lapiz = os.sys.argv[2]
nro_lapiz = 0
for lapiz in tipos_de_lapiz:
    print(lapiz)
    nro_lapiz +=1
    if nro_lapiz <5:
        print("malo")
#fin_for
print("los tipos son:",nro_lapiz)
