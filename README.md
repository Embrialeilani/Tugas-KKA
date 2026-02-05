# Praktikum OOP Python Kelas XI

---

## Identitas
**Nama** : Embria Leilani Shanawa<br>
**Kelas** : XI RPL 5<br>
**Mapel** : Kodinng & Kecerdasan Artifisial

---

## Praktikum 1 - Abstraction_interface
Praktikum ini bertujuan untuk memahami penggunaan abstract class dan inheritance pada Python. Kelas GameUnit digunakan sebagai abstract class yang memiliki metode serang() dan info(). Kelas Hero dan Monster merupakan kelas turunan yang mengimplementasikan metode tersebut dengan cara berbeda.
Program menunjukkan konsep polimorfisme, karena metode yang sama dapat menghasilkan output yang berbeda tergantung objek yang digunakan.

**Hasil Output**
Saya adalah Hero: Alucard 
Saya adalah Monster: Serigala
Hero Alucard menebas Monster!
Monster Serigala menggigit Hero!

---

## Praktikum 2 - Enkapsulasi_hp
Praktikum ini bertujuan untuk memahami konsep encapsulation (enkapsulasi) dalam Python. Atribut __hp dibuat bersifat private agar tidak bisa diubah langsung dari luar kelas. Akses dan perubahan nilai HP hanya bisa dilakukan melalui getter dan setter.Setter digunakan untuk membatasi nilai HP agar tetap valid.

**Hasil Output**
0
Mencoba akses paksa: 0

---

## Praktikum 3 - Game_rpg
Praktikum ini bertujuan untuk memahami konsep inheritance dan method overriding. Kelas Mage merupakan turunan dari kelas Hero yang memiliki atribut tambahan mana dan skill khusus skill_fireball().
Metode info() dioverride untuk menampilkan informasi berbeda.

**Hasil Output**
--- Update Class Hero ---
Lylia [Mage] | HP: 80 | Mana: 100
Lylia menyerang Balmond!
Balmond terkena damage 30. Sisa HP: 170
Lylia menggunakan Fireball ke Balmond!
Balmond terkena damage 60. Sisa HP: 110

--- Pertarungan Dimulai ---
Layla menyerang Zilong!
Zilong terkena damage 15. Sisa HP: 105
Zilong menyerang Layla!
Layla terkena damage 20. Sisa HP: 80

---

## Praktikum 4 - Polymorphism
Praktikum ini bertujuan untuk memahami konsep polymorphism. Kelas Mage, Archer, dan Fighter merupakan turunan dari kelas Hero dan mengoverride metode serang(). Walaupun metode yang dipanggil sama, setiap objek menghasilkan perilaku yang berbeda.

**Hasil Output**
--- PERANG DIMULAI ---
Eudora (Mage) menembakkan Bola Api! Boom!
Miya (Archer) memanah dari jauh! Jleb!
Zilong (Fighter) memukul dengan pedang! Slash!
Gord (Mage) menembakkan Bola Api! Boom!

---

## Praktikum kelompok - Techmaster
Praktikum ini bertujuan untuk menerapkan seluruh konsep Object-Oriented Programming (OOP), yaitu abstraction, encapsulation, inheritance, dan polymorphism. Kelas abstrak BarangElektronik digunakan sebagai dasar, sedangkan Laptop dan Smartphone merupakan kelas turunan dengan perhitungan pajak berbeda. Atribut dibuat private untuk menjaga keamanan data, dan polimorfisme diterapkan dalam proses transaksi.

**Hasil Output**
--- SETUP DATA ---
Berhasil menambahkan stok ROG Zephyrus: 10 unit.
Gagal update stok iPhone 13! Stok tidak boleh negatif (-5).
Berhasil menambahkan stok iPhone 13: 20 unit.

--- STRUK TRANSAKSI ---
1. [LAPTOP] ROG Zephyrus | Proc: Ryzen 9
   Harga Dasar: Rp 20,000,000 | Pajak(10%): Rp 2,000,000
   Beli: 2 unit | Subtotal: Rp 44,000,000

2. [SMARTPHONE] iPhone 13 | Cam: 12MP
   Harga Dasar: Rp 15,000,000 | Pajak(5%): Rp 750,000
   Beli: 1 unit | Subtotal: Rp 15,750,000

----------------------------------------
TOTAL TAGIHAN: Rp 59,750,000
----------------------------------------

---

## Kesimpulan
Bahwa konsep Object-Oriented Programming (OOP) membantu membuat program lebih terstruktur dan mudah dipahami. Penerapan class, encapsulation, inheritance, polymorphism, dan abstraction membuat program lebih rapi, aman, serta mudah dikembangkan.





















