a=[84, 104, 105, 115, 32, 101, 120, 101, 114, 99, 105, 99,
101, 32, 105, 115, 32, 97, 119, 101, 115, 111, 109,
101, 32, 33]
def Ascii (liste):
    b=[0]*(len(liste)-1)
    for i in range(len(liste)-1) :
        b[i]=chr(liste[i])
        
    return ''.join(b)

print(Ascii(a))