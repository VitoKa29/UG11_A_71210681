def ambil_tengah(string, tambah = 0):
    if(tambah):
        count = len(string)
        bagi = (count // 2)
        return(string[bagi+tambah])
    else:
        count = len(string)
        bagi = (count // 2)
        return(string[bagi])

print(ambil_tengah("abcdefg",1))
print(ambil_tengah("abcdefg",2))
print(ambil_tengah("abcd"))