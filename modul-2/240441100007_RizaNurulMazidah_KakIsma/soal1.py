class MataKuliah:
    def __init__(self, kode_matkul, nama_matkul, sks):
        if MataKuliah.cek_sks_valid(sks):
            self.kode_matkul = kode_matkul
            self.nama_matkul = nama_matkul
            self.sks = sks
        else:
            print(f"SKS {sks} tidak valid untuk mata kuliah {nama_matkul}. SKS harus 2 atau 3.")

    @staticmethod
    def cek_sks_valid(sks):
        return sks == 2 or sks == 3

    def __str__(self):
        return f"{self.kode_matkul} - {self.nama_matkul} ({self.sks} SKS)"

class Kampus:
    total_mahasiswa = 0

    def __init__(self, nama_kampus, alamat_kampus):
        if self.cek_nama_kampus(nama_kampus):
            self.nama_kampus = nama_kampus
            self.alamat_kampus = alamat_kampus
        else:
            print(f"Nama kampus {nama_kampus} tidak valid. Nama kampus tidak boleh mengandung angka.")

    def tampilkan_info(self):
        return f"Kampus: {self.nama_kampus}, Alamat: {self.alamat_kampus}, Total Mahasiswa: {Kampus.total_mahasiswa}"

    @staticmethod
    def cek_nama_kampus(nama_kampus):
        if any(char.isdigit() for char in nama_kampus):
            return False
        return True

class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if self.validasi_nim(nim):
            self.nama = nama
            self.nim = nim
            self.prodi = prodi
            self.matkul_diambil = []
            Mahasiswa.jumlah_mahasiswa += 1
            Kampus.total_mahasiswa += 1 
        else:
            print(f"NIM {nim} tidak valid. NIM harus diawali dengan '23' dan terdiri dari 10 digit.")
            self.nim = "NIM TIDAK VALID"

    def tambah_mata_kuliah(self, matkul):
        if matkul is not None:
            self.matkul_diambil.append(matkul)

    def hitung_total_sks(self):
        total = 0
        for matkul in self.matkul_diambil:
            total += matkul.sks
        return total

    def tampilkan_biodata(self):
        print(f"\nBiodata Mahasiswa:")
        print(f"NAMA: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"PROGRAM STUDI: {self.prodi}")
        print("MATA KULIAH YANG DIAMBIL:")
        for mk in self.matkul_diambil:
            print(f"  - {mk}")
        print(f"TOTAL SKS YANG DIAMBIL: {self.hitung_total_sks()}")

    @classmethod
    def get_jumlah_mahasiswa(cls):
        return cls.jumlah_mahasiswa

    @staticmethod
    def validasi_nim(nim):
        if len(nim) == 10 and nim[:2] == "23" and nim.isdigit():
            return True
        return False

    def __str__(self):
        return f"{self.nama} ({self.nim}) - {self.prodi}"

# 8 Mata Kuliah
mata_kuliah1 = MataKuliah("MK101", "Pemrograman Berbasis Objek", 3)
mata_kuliah2 = MataKuliah("MK102", "Pemrograman Berbasis Web", 3)
mata_kuliah3 = MataKuliah("MK103", "Pengantar Basis Data", 3)
mata_kuliah4 = MataKuliah("MK104", "Desain Manajemen Jaringan", 2)
mata_kuliah5 = MataKuliah("MK105", "Analisa Proses Bisnis", 2)
mata_kuliah6 = MataKuliah("MK106", "Algoritma Pemrograman", 3)
mata_kuliah7 = MataKuliah("MK107", "Statistik", 2)
mata_kuliah8 = MataKuliah("MK108", "E-Bussines & E-Commerce", 2)

# 6 Mahasiswa
mhs1 = Mahasiswa("Jihan", "2312345678", "Teknik Informatika")
mhs2 = Mahasiswa("Riza", "2312345679", "Sistem Informasi")
mhs3 = Mahasiswa("Nurisya", "2312345680", "Teknik Industri")
mhs4 = Mahasiswa("Zahra", "2312345681", "Teknik Mekatronika")
mhs5 = Mahasiswa("Martha", "2312345682", "Sistem Informasi")
mhs6 = Mahasiswa("Desi", "2312345683", "Akutansi")

# Tambah Mata Kuliah ke Mahasiswa
mhs1.tambah_mata_kuliah(mata_kuliah2)
mhs1.tambah_mata_kuliah(mata_kuliah3)
mhs1.tambah_mata_kuliah(mata_kuliah5)
mhs1.tambah_mata_kuliah(mata_kuliah6)

mhs2.tambah_mata_kuliah(mata_kuliah1)
mhs2.tambah_mata_kuliah(mata_kuliah4)
mhs2.tambah_mata_kuliah(mata_kuliah7)
mhs2.tambah_mata_kuliah(mata_kuliah8)

mhs3.tambah_mata_kuliah(mata_kuliah1)
mhs3.tambah_mata_kuliah(mata_kuliah4)
mhs3.tambah_mata_kuliah(mata_kuliah5)
mhs3.tambah_mata_kuliah(mata_kuliah6)

mhs4.tambah_mata_kuliah(mata_kuliah2)
mhs4.tambah_mata_kuliah(mata_kuliah4)
mhs4.tambah_mata_kuliah(mata_kuliah5)
mhs4.tambah_mata_kuliah(mata_kuliah8)

mhs5.tambah_mata_kuliah(mata_kuliah1)
mhs5.tambah_mata_kuliah(mata_kuliah3)
mhs5.tambah_mata_kuliah(mata_kuliah7)
mhs5.tambah_mata_kuliah(mata_kuliah6)

mhs6.tambah_mata_kuliah(mata_kuliah2)
mhs6.tambah_mata_kuliah(mata_kuliah5)
mhs6.tambah_mata_kuliah(mata_kuliah6)
mhs6.tambah_mata_kuliah(mata_kuliah8)

# Kampus
kampus = Kampus("Universitas Trunojoyo 5", "Jl. Trunojoyo") 

# Menampilkan Data Mahasiswa
print("\n===== DATA MAHASISWA =====")
for mahasiswa in [mhs1, mhs2, mhs3, mhs4, mhs5, mhs6]:
    mahasiswa.tampilkan_biodata()
    print("-------------------------------------------------------")

# Menampilkan Info Kampus
print("\n===== INFO KAMPUS =====")
print(kampus.tampilkan_info())