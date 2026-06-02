from abc import ABC, abstractmethod

class Koleksi(ABC):
    def __init__(self, kode, judul, tahun_terbit, penerbit):
        self.kode = kode
        self.judul = judul
        self.tahun_terbit = tahun_terbit
        self.penerbit = penerbit
    @abstractmethod
    def tampil_info(self):
        pass
