kalimat = input("Masukkan Kalimat: ")
start = int(input("Index Start: "))
stop = int(input("Index Stop: "))

def hitung_hapus(kalimat, start, stop):
    count_asli = len(kalimat)
    count_hapus = len(kalimat[start-1:stop])
    persentase = (count_hapus / count_asli) * 100
    return persentase

print(hitung_hapus(kalimat, start, stop))