def PangkatPositif(x, y, z):
    if y > 1:
        x *= z
        y-=1
        return PangkatPositif(x, y, z)
    else:
        return x

def PangkatNegativ(x, y ,z):
    if y < -1:
        x *= z
        y+=1
        return PangkatNegativ(x, y, z)
    else:
        return 1/x

def CekPangkat(x, y, z):
    if y == 0:
        print(1)
    elif y > 0:
        print(PangkatPositif(x, y, z))
    else:
        print(PangkatNegativ(x, y, z))

while True:
    angka = input("Angka: ")
    if angka == "":
        break
    angka = float(angka)
    pangkat = int(input("Pangkat: "))
    CekPangkat(angka, pangkat, angka)
    
print("byee")