from koleksi_base import Koleksi
class Buku(Koleksi):
    def _init_(self, kode, judul, tahun_terbit, penerbit, pengarang):
        super()._init_(kode, judul, tahun_terbit, penerbit)
        self.pengarang = pengarang

    def tampil_info(self):
        print(f"Thn Terbit    : {self.tahun_terbit}")
        print(f"Pengarang     : {self.pengarang}")
        print(f"Penerbit      : {self.penerbit}")


class Majalah(Koleksi):
    def _init_(self, kode, judul, tahun_terbit, penerbit, edisi):
        super()._init_(kode, judul, tahun_terbit, penerbit)
        self.edisi = edisi

    def tampil_info(self):
        print(f"Tahun Terbit  : {self.tahun_terbit}")
        print(f"Penerbit      : {self.penerbit}")
        print(f"Edisi         : {self.edisi}")
