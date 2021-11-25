print("="*8,"Calculator Sederhana","="*8)
print("1. Pertambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Pangkat \n")

pilihan = int(input("Masukkan pilihan: "))
bilangan1 = int(input("Masukkan bilangan 1: "))
bilangan2 = int(input("Masukkan bilangan 2: "))

def calculator(pilihan):
    if(pilihan == 1):
        print("Hasilnya:", tambah(bilangan1, bilangan2))
    elif(pilihan == 2):
        print("Hasilnya:", kurang(bilangan1, bilangan2))
    elif(pilihan == 3):
        print("Hasilnya:", kali(bilangan1, bilangan2))
    elif(pilihan == 4):
        print("Hasilnya:", bagi(bilangan1, bilangan2))
    elif(pilihan == 5):
        print("Hasilnya:", pangkat(bilangan1, bilangan2))
    else:
        print("Hasilnya: Maaf input operasi antara 1-5")
def tambah(bilangan1, bilangan2):
    tambah = bilangan1 + bilangan2
    return tambah
def kurang(bilangan1, bilangan2):
    kurang = bilangan1 - bilangan2
    return kurang
def bagi(bilangan1, bilangan2):
    bagi = bilangan1 / bilangan2
    return bagi
def kali(bilangan1, bilangan2):
    kali = bilangan1 * bilangan2
    return kali
def pangkat(bilangan1, bilangan2):
    pangkat = bilangan1 ** bilangan2
    return pangkat

calculator(pilihan)