class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
    
    def berjalan(self):
        print(f"{self.nama} sedang berjalan di trotoar")

    def berlari(self):
        print(f"{self.nama} sedang berlari di lapangan")

# membuat objek
Manusia1 = Manusia("Riza", 18, "Lamongan")
Manusia2 = Manusia("Risa", 19, "Sampang")
Manusia3 = Manusia("Jihan", 19, "Bangkalan")
Manusia4 = Manusia("Zahra", 15, "Mojokerto")
Manusia5 = Manusia("Wildan", 20, "Sidoarjo")
Manusia6 = Manusia("Andre", 21, "Surabaya")
Manusia7 = Manusia("Budi", 8, "Jakarta")

# mengakses atribut dan method
print("NAMA  : ", Manusia1.nama)
print("UMUR  : ", Manusia1.umur)
print("ALAMAT: ", Manusia1.alamat)
Manusia1.berjalan()
Manusia1.berlari()
print()

print("NAMA  : ", Manusia2.nama)
print("UMUR  : ", Manusia2.umur)
print("ALAMAT: ", Manusia2.alamat)
Manusia2.berjalan()
Manusia2.berlari()
print()

print("NAMA  : ", Manusia3.nama)
print("UMUR  : ", Manusia3.umur)
print("ALAMAT: ", Manusia3.alamat)
Manusia3.berjalan()
Manusia3.berlari()
print()

print("NAMA  : ", Manusia4.nama)
print("UMUR  : ", Manusia4.umur)
print("ALAMAT: ", Manusia4.alamat)
Manusia4.berjalan()
Manusia4.berlari()
print()

print("NAMA  : ", Manusia5.nama)
print("UMUR  : ", Manusia5.umur)
print("ALAMAT: ", Manusia5.alamat)
Manusia5.berjalan()
Manusia5.berlari()
print()

print("NAMA  : ", Manusia6.nama)
print("UMUR  : ", Manusia6.umur)
print("ALAMAT: ", Manusia6.alamat)
Manusia6.berjalan()
Manusia6.berlari()
print()

print("NAMA  : ", Manusia7.nama)
print("UMUR  : ", Manusia7.umur)
print("ALAMAT: ", Manusia7.alamat)
Manusia7.berjalan()
Manusia7.berlari()
print()