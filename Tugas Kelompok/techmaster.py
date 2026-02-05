from abc import ABC, abstractmethod

# ==============================
# ABSTRACT CLASS (ABSTRACTION)
# ==============================
class BarangElektronik(ABC):
    def __init__(self, nama, harga_dasar):
        self.nama = nama
        self.__stok = 0               # Private attribute
        self.__harga_dasar = harga_dasar  # Private attribute

    # GETTER
    def get_stok(self):
        return self.__stok

    def get_harga_dasar(self):
        return self.__harga_dasar

    # SETTER / VALIDATOR
    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {self.__stok} unit.")

    @abstractmethod
    def tampilkan_detail(self, jumlah):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass


# ==============================
# CHILD CLASS: LAPTOP
# ==============================
class Laptop(BarangElektronik):
    def __init__(self, nama, harga_dasar, processor):
        super().__init__(nama, harga_dasar)
        self.processor = processor

    def hitung_harga_total(self, jumlah):
        pajak = 0.10 * self.get_harga_dasar()
        return (self.get_harga_dasar() + pajak) * jumlah

    def tampilkan_detail(self, jumlah):
        pajak = 0.10 * self.get_harga_dasar()
        subtotal = self.hitung_harga_total(jumlah)
        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")
        print(f"   Harga Dasar: Rp {self.get_harga_dasar():,} | Pajak(10%): Rp {int(pajak):,}")
        print(f"   Beli: {jumlah} unit | Subtotal: Rp {int(subtotal):,}\n")


# ==============================
# CHILD CLASS: SMARTPHONE
# ==============================
class Smartphone(BarangElektronik):
    def __init__(self, nama, harga_dasar, kamera):
        super().__init__(nama, harga_dasar)
        self.kamera = kamera

    def hitung_harga_total(self, jumlah):
        pajak = 0.05 * self.get_harga_dasar()
        return (self.get_harga_dasar() + pajak) * jumlah

    def tampilkan_detail(self, jumlah):
        pajak = 0.05 * self.get_harga_dasar()
        subtotal = self.hitung_harga_total(jumlah)
        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")
        print(f"   Harga Dasar: Rp {self.get_harga_dasar():,} | Pajak(5%): Rp {int(pajak):,}")
        print(f"   Beli: {jumlah} unit | Subtotal: Rp {int(subtotal):,}\n")


# ==============================
# POLYMORPHISM FUNCTION
# ==============================
def proses_transaksi(keranjang):
    print("\n--- STRUK TRANSAKSI ---")
    total = 0
    for i, (barang, jumlah) in enumerate(keranjang, start=1):
        print(f"{i}. ", end="")
        barang.tampilkan_detail(jumlah)
        total += barang.hitung_harga_total(jumlah)

    print("----------------------------------------")
    print(f"TOTAL TAGIHAN: Rp {int(total):,}")
    print("----------------------------------------")


# ==============================
# MAIN PROGRAM (USER STORY)
# ==============================
print("--- SETUP DATA ---")

laptop1 = Laptop("ROG Zephyrus", 20_000_000, "Ryzen 9")
hp1 = Smartphone("iPhone 13", 15_000_000, "12MP")

laptop1.tambah_stok(10)
hp1.tambah_stok(-5)      # Gagal
hp1.tambah_stok(20)

keranjang_belanja = [
    (laptop1, 2),
    (hp1, 1)
]

proses_transaksi(keranjang_belanja)