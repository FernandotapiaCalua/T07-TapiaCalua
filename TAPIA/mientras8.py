import os
base=  int(os.sys.argv[1])
altura=  int(os.sys.argv[2])
area= (base*altura)/2
while area<40:
    print("altura exacta")
    base=  int(os.sys.argv[3])
    altura=  int(os.sys.argv[4])
    area= (base*altura)/2
if area >40:
    print("el area no correcta")
#fin_mientras
