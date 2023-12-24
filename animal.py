class Hewan:
    def __init__(self, nama, makanan, habitat, metode_reproduksi):
        self.nama = nama
        self.makanan = makanan
        self.habitat = habitat
        self.metode_reproduksi = metode_reproduksi

    def makan(self):
        print(f"{self.nama} sedang makan {self.makanan}")

    def tidur(self):
        print(f"{self.nama} sedang tidur")


class Badak(Hewan):
    def __init__(self, nama, makanan, habitat, metode_reproduksi, warna_kulit):
        super().__init__(nama, makanan, habitat, metode_reproduksi)
        self.warna_kulit = warna_kulit

    def bersuara(self):
        print(f"{self.nama} mengeluarkan suara")


class Ikan(Hewan):
    def __init__(self, nama, makanan, habitat, metode_reproduksi, jenis_ikan):
        super().__init__(nama, makanan, habitat, metode_reproduksi)
        self.jenis_ikan = jenis_ikan

    def berenang(self):
        print(f"{self.nama} sedang berenang")


class Ular(Hewan):
    def __init__(self, nama, makanan, habitat, metode_reproduksi, panjang):
        super().__init__(nama, makanan, habitat, metode_reproduksi)
        self.panjang = panjang

    def melata(self):
        print(f"{self.nama} sedang melata")


# Contoh penggunaan
badak = Badak("Badak Jawa", "tumbuhan", "darat", "melahirkan", "hitam")
badak.makan()
badak.bersuara()

ikan = Ikan("Ikan Mas", "plankton", "air", "bertelur", "mas")
ikan.berenang()

ular = Ular("Ular Piton", "tikus", "darat", "melahirkan", "4 meter")
ular.melata()
