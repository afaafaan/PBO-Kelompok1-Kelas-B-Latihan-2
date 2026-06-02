import unittest
# Mengimport file utama yang dibuat oleh anggota kelompok lain
from manager import LibraryManager
from subclasses import Buku, Majalah, Jurnal

class TestLibrarySystem(unittest.TestCase):
    
    def setUp(self):
        """Menyiapkan environment testing sebelum setiap pengujian berjalan"""
        self.manager = LibraryManager()
        self.buku_test = Buku("B01", "Laskar Pelangi", "2005", "Bentang Pustaka", "Andrea Hirata")
        self.majalah_test = Majalah("M01", "Bobo", "2023", "Kompas Gramedia", "Edisi 50")

    def test_tambah_data_sukses(self):
        """Memastikan data baru bisa ditambahkan ke dalam sistem"""
        # Awalnya data kosong
        self.assertEqual(len(self.manager.daftar_koleksi), 0)
        
        # Tambah data buku
        berhasil = self.manager.tambah_data(self.buku_test)
        self.assertTrue(berhasil)
        self.assertEqual(len(self.manager.daftar_koleksi), 1)

    def test_tambah_data_duplikat(self):
        """Memastikan sistem menolak jika ada Kode Koleksi yang sama (Validasi SOLID)"""
        self.manager.tambah_data(self.buku_test)
        
        # Mencoba menambahkan buku lain tapi dengan kode "B01" yang sama
        buku_duplikat = Buku("B01", "Buku Palsu", "2026", "Penerbit X", "Anonim")
        gagal = self.manager.tambah_data(buku_duplikat)
        
        # Harus menghasilkan False (gagal ditambah)
        self.assertFalse(gagal)
        self.assertEqual(len(self.manager.daftar_koleksi), 1)

    def test_hapus_data_sukses(self):
        """Memastikan data bisa dihapus berdasarkan kode koleksinya"""
        self.manager.tambah_data(self.buku_test)
        
        # Hapus kode B01
        terhapus = self.manager.hapus_data("B01")
        self.assertTrue(terhapus)
        self.assertEqual(len(self.manager.daftar_koleksi), 0)

if __name__ == "__main__":
    unittest.main()