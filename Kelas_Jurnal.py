class Jurnal(Koleksi):

    def __init__(self, kode, judul, tahun_terbit,
                 penerbit, bidang_studi, impact_factor):
        super().__init__(kode, judul, tahun_terbit, penerbit)

        self.bidang_studi = bidang_studi
        self.impact_factor = impact_factor
    def tampil_info(self):
        print(f"Kode          : {self.kode}")
        print(f"Judul         : {self.judul}")
        print(f"Tahun Terbit  : {self.tahun_terbit}")
        print(f"Penerbit      : {self.penerbit}")
        print(f"Bidang Studi  : {self.bidang_studi}")
        print(f"Impact Factor : {self.impact_factor}")