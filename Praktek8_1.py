ulang = int(input("Jumblah angka: "))

def Penjumblahan(x):
    if x <= 0:
        return 0
    else:
        angka = float(input(f"masukkan angka ke{x} "))
        return angka + Penjumblahan(x - 1)
    
print(f"hasil: {Penjumblahan(ulang)}")