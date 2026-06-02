class LibraryManager:
    def __init__(self):
        self.daftar_koleksi = []

    def tambah_data(self, objek_koleksi):
        self.daftar_koleksi.append(objek_koleksi)

    def hapus_data(self, kode):
        for data in self.daftar_koleksi:
            if data.kode == kode:
                self.daftar_koleksi.remove(data)
                print("---------------------------------------")
                print("Hapus data koleksi sukses")
                return True
        print("---------------------------------------")
        print("Kode koleksi tidak ditemukan!")
        return False

    def tampil_semua_data(self):
        if not self.daftar_koleksi:
            print("Belum ada data koleksi.")
            return

        print("=======================================")
        print("DATA KOLEKSI\n")
        
    
        for i, data in enumerate(self.daftar_koleksi, 1):
            print(f"Koleksi {i}:")
            print(f"Jenis         : {data.__class__.__name__}")
            print(f"Kode Koleksi  : {data.kode}")
            print(f"Judul         : {data.judul}")
            data.tampil_info() 
            print()
            print("=======================================")