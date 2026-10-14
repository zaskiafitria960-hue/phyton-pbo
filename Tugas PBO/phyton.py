"""
Sistem Penggajian Karyawan (Payroll System)
Materi: Class, Encapsulation, Inheritance, Polymorphism
(Versi dengan komentar penjelasan di setiap bagian)
"""


# ==========================================================
# 1. SUPERCLASS: Karyawan (class induk / cetakan dasar)
# ==========================================================
class Karyawan:  # Membuat class bernama Karyawan, berisi data & perilaku umum semua karyawan

    # Constructor: otomatis dijalankan saat objek dibuat
    def __init__(self, nama, id_karyawan, gaji_pokok):  # self = objek itu sendiri; sisanya data yang dikirim saat membuat objek
        self.nama = nama                    # Atribut PUBLIC: bisa diakses langsung dari luar class
        self.id_karyawan = id_karyawan      # Atribut PUBLIC: ID unik karyawan
        self.__gaji_pokok = gaji_pokok      # Atribut PRIVATE (diawali "__"): tidak bisa diakses langsung dari luar class

    # ---------- GETTER ----------
    def get_gaji_pokok(self):               # Getter: pintu resmi untuk MELIHAT gaji pokok
        return self.__gaji_pokok            # Mengembalikan nilai gaji pokok yang disimpan secara private

    # ---------- SETTER ----------
    def set_gaji_pokok(self, gaji_pokok):   # Setter: pintu resmi untuk MENGUBAH gaji pokok
        if gaji_pokok <= 0:                 # Validasi: cek apakah nilai baru tidak masuk akal (nol atau negatif)
            print("Peringatan: Gaji pokok harus lebih besar dari 0! "
                  "Perubahan dibatalkan.")  # Tampilkan pesan peringatan, gaji TIDAK diubah
        else:                               # Kalau nilainya valid (lebih dari 0)
            self.__gaji_pokok = gaji_pokok  # Maka gaji pokok diperbarui dengan nilai baru

    # ---------- HITUNG GAJI (implementasi dasar) ----------
    def hitung_gaji_total(self):            # Method untuk menghitung total gaji
        return self.__gaji_pokok            # Untuk karyawan umum, total gaji = gaji pokok saja

    # ---------- TAMPILKAN INFO ----------
    def tampilkan_info(self):               # Method untuk menampilkan data karyawan ke layar
        print(f"Nama          : {self.nama}")                    # Cetak nama karyawan
        print(f"ID Karyawan   : {self.id_karyawan}")             # Cetak ID karyawan
        print(f"Gaji Pokok    : Rp{self.__gaji_pokok:,.0f}")     # Cetak gaji pokok; ":,.0f" = format ribuan tanpa desimal


# ==========================================================
# 2. CHILD CLASS: KaryawanTetap (INHERITANCE dari Karyawan)
# ==========================================================
class KaryawanTetap(Karyawan):              # Tanda (Karyawan) artinya mewarisi semua atribut & method dari Karyawan

    def __init__(self, nama, id_karyawan, gaji_pokok, tunjangan):  # Constructor dengan tambahan parameter tunjangan
        super().__init__(nama, id_karyawan, gaji_pokok)  # Panggil constructor induk untuk mengisi nama, ID, dan gaji pokok
        self.tunjangan = tunjangan          # Atribut tambahan khusus karyawan tetap (public)

    # OVERRIDING: menulis ulang method milik induk dengan cara hitung yang berbeda
    def hitung_gaji_total(self):
        return self.get_gaji_pokok() + self.tunjangan  # Gaji total = gaji pokok + tunjangan (pakai getter karena gaji pokok private)

    # OVERRIDING: menampilkan info yang lebih lengkap dari versi induk
    def tampilkan_info(self):
        print("=== Karyawan Tetap ===")     # Judul penanda jenis karyawan
        super().tampilkan_info()             # Panggil tampilkan_info milik induk (nama, ID, gaji pokok) agar tidak menulis ulang
        print(f"Tunjangan     : Rp{self.tunjangan:,.0f}")             # Tambahan: tampilkan tunjangan
        print(f"Total Gaji    : Rp{self.hitung_gaji_total():,.0f}")   # Tambahan: tampilkan total gaji hasil perhitungan


# ==========================================================
# 3. CHILD CLASS: KaryawanKontrak (INHERITANCE dari Karyawan)
# ==========================================================
class KaryawanKontrak(Karyawan):            # Juga mewarisi dari Karyawan

    def __init__(self, nama, id_karyawan, gaji_pokok, jam_lembur, tarif_lembur):  # Constructor dengan data lembur
        super().__init__(nama, id_karyawan, gaji_pokok)  # Isi data umum lewat constructor induk
        self.jam_lembur = jam_lembur        # Atribut tambahan: total jam lembur sebulan
        self.tarif_lembur = tarif_lembur    # Atribut tambahan: tarif upah per jam lembur

    # OVERRIDING: rumus gaji berbeda dari karyawan tetap
    def hitung_gaji_total(self):
        return self.get_gaji_pokok() + (self.jam_lembur * self.tarif_lembur)  # Gaji total = gaji pokok + (jam lembur x tarif lembur)

    # OVERRIDING: tampilkan rincian lembur
    def tampilkan_info(self):
        total_lembur = self.jam_lembur * self.tarif_lembur  # Hitung dulu upah lembur total (disimpan di variabel agar mudah dipakai)
        print("=== Karyawan Kontrak ===")  # Judul penanda jenis karyawan
        super().tampilkan_info()             # Panggil info dasar milik induk (nama, ID, gaji pokok)
        print(f"Jam Lembur    : {self.jam_lembur} jam")                 # Tampilkan jumlah jam lembur
        print(f"Tarif Lembur  : Rp{self.tarif_lembur:,.0f}/jam")        # Tampilkan tarif per jam
        print(f"Total Lembur  : Rp{total_lembur:,.0f}")                 # Tampilkan total upah lembur
        print(f"Total Gaji    : Rp{self.hitung_gaji_total():,.0f}")     # Tampilkan total gaji keseluruhan


# ==========================================================
# MAIN PROGRAM (bagian yang dijalankan untuk pengujian)
# ==========================================================
if __name__ == "__main__":                  # Kode di bawah hanya jalan jika file ini dijalankan langsung (bukan di-import)

    # 1. Membuat objek dari masing-masing class
    karyawan_tetap = KaryawanTetap("Akmal Nuryazid", "KT-001", 8000000, 2000000)    # Objek karyawan tetap: gaji pokok 8 juta, tunjangan 2 juta
    karyawan_kontrak = KaryawanKontrak("Zaskia Fitria Ramadhani", "KK-001", 5000000, 20, 50000)  # Objek karyawan kontrak: gaji pokok 5 juta, lembur 20 jam @ Rp50.000

    # 2. Menyimpan kedua objek ke dalam satu list
    daftar_karyawan = [karyawan_tetap, karyawan_kontrak]  # List ini berisi dua jenis objek berbeda, tapi dianggap sama-sama "karyawan"

    # 3. Demonstrasi POLYMORPHISM
    print("########## DEMONSTRASI POLYMORPHISM ##########\n")  # Judul bagian demo
    for karyawan in daftar_karyawan:        # Looping: ambil objek satu per satu dari list
        karyawan.tampilkan_info()           # Perintahnya SAMA, tapi hasilnya BEDA tergantung jenis objek (itulah polymorphism)
        print()                             # Cetak baris kosong sebagai pemisah antar karyawan

    # 4. Demonstrasi ENCAPSULATION
    print("########## DEMONSTRASI ENCAPSULATION ##########\n")  # Judul bagian demo

    print(f"Gaji pokok {karyawan_tetap.nama} sebelum diubah: "
          f"Rp{karyawan_tetap.get_gaji_pokok():,.0f}")  # Tampilkan gaji awal lewat getter

    print("\n[1] Mengubah gaji pokok dengan nilai TIDAK valid (-1000000):")
    karyawan_tetap.set_gaji_pokok(-1000000)  # Coba ubah ke nilai negatif -> ditolak setter, muncul peringatan

    print("\n[2] Mengubah gaji pokok dengan nilai VALID (9000000):")
    karyawan_tetap.set_gaji_pokok(9000000)   # Ubah ke nilai valid -> diterima, gaji pokok berubah

    print("\nInfo karyawan setelah perubahan:\n")
    karyawan_tetap.tampilkan_info()          # Tampilkan ulang: gaji pokok dan total gaji sudah ikut berubah