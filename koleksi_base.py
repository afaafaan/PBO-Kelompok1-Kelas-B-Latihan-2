from abc import ABC, abstractmethod

class Koleksi(ABC):
    def _init_(self, kode, judul, tahun_terbit, penerbit):
        self.kode = kode
        self.judul = judul
        self.tahun_terbit = tahun_terbit
        self.penerbit = penerbit

    # ABSTRAKSI & POLIMORFISME: 
    # Semua kelas anak wajib mengimplementasikan fungsi ini dengan cara mereka sendiri
    @abstractmethod
    def tampil_info(self):
        pass