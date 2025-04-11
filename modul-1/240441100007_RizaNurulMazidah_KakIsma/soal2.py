class Mahasiswa:
    def __init__(self, nama, nim, prodi, fakultas, alamat):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.fakultas = fakultas
        self.alamat = alamat

    def infoMahasiswa(self):
        print("NAMA    : ", self.nama)
        print("NIM     : ", self.nim)
        print("PRODI   : ", self.prodi)
        print("FAKULTAS: ", self.fakultas)
        print("ALAMAT  : ", self.alamat)
        print()

# menyimpan data mahasiswa dalam list
data_mahasiswa = []

# loop untuk meminta input data mahasiswa
for i in range(3):
    print(f"---MASUKKAN DATA MAHASISWA KE-{i+1}---")
    nama = input("NAMA: ")
    nim = input("NIM: ")
    prodi = input("PRODI: ")
    fakultas = input("FAKULTAS: ")
    alamat = input("ALAMAT: ")
    print()

    mahasiswa = Mahasiswa(nama, nim, prodi, fakultas, alamat)
    data_mahasiswa += [mahasiswa]

# menampilkan data mahasiswa
print("---DATA MAHASISWA---")
for mahasiswa in data_mahasiswa:
    mahasiswa.infoMahasiswa()