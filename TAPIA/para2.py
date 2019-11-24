import os
ñ = int(os.sys.argv[1])
l = int(os.sys.argv[2])
m= ñ*l
while m > 20:
    print(m,"no acuerdo")
    ñ=ñ+1
    if m < 20:
        print("de acuerdo")
