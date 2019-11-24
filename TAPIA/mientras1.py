import os
base= int(os.sys.argv[1])
altura= int(os.sys.argv[2])
area= (base * altura)/2
while area>=25:
    print("area mayor igual a 15")
    base= int(os.sys.argv[3])
    altura= int(os.sys.argv[4])
    area= (base * altura)/2
if area<25:
    print("area menor a 15:",area)
#fin_while
