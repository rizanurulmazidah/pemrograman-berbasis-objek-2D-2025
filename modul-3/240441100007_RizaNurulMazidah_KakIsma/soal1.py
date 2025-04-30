class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Gaji: {self.gaji}")
        print(f"Departemen: {self.departemen}")

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        super().info()
        print(f"Tunjangan: {self.tunjangan}")
        print("Status: Karyawan Tetap\n")

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        super().info()
        print(f"Jam Kerja per Hari: {self.jam_kerja}")
        print("Status: Karyawan Harian\n")

class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        for karyawan in self.daftar_karyawan:
            karyawan.info()

# Membuat objek ManajemenKaryawan
manajemen = ManajemenKaryawan()

# Menambahkan beberapa karyawan
karyawan1 = KaryawanTetap("Riza", 7000000, "Keuangan", 3500000)
karyawan2 = KaryawanHarian("Desi", 2000000, "Gudang", 8)
karyawan3 = KaryawanTetap("Risa", 8000000, "IT", 4000000)
karyawan4 = KaryawanHarian("Jihan", 600000, "Marketing", 8)
karyawan5 = KaryawanTetap("Martha", 5000000, "Produksi", 1500000)

manajemen.tambah_karyawan(karyawan1)
manajemen.tambah_karyawan(karyawan2)
manajemen.tambah_karyawan(karyawan3)
manajemen.tambah_karyawan(karyawan4)
manajemen.tambah_karyawan(karyawan5)

# Menampilkan semua karyawan
manajemen.tampilkan_semua_karyawan()
