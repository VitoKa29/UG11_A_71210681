def ambildanbalik(string, start, stop, validity):
    if(validity):
        kata = string[start-1:stop]
        return(kata[::-1])
    elif(not validity):
        return(string[start-1:stop])
    else:
        return("Maaf, salah input")

print(ambildanbalik("abcdefg",2,4,True))
print(ambildanbalik("abcdefg",1,5,False))
print(ambildanbalik("Qwerty",3,4,True))
print(ambildanbalik("Qwerty",2,2,False))