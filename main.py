daftar_koleksi = []

def menu():

    global daftar_koleksi 
    
    while True:
        print(" ")
        print("="*20)
        print("MENU PROGRAM")
        print("-"*20)
        print("1. Tambah data koleksi")
        print("2. Hapus data koleksi")
        print("3. Tampil semua data koleksi")
        print("4. Keluar")
        
        pilih = input("Nomor yang dipilih: ")

        if pilih == '1':
            print("\nJENIS KOLEKSI YANG AKAN DITAMBAH")
            print("1. Buku\n2. Majalah\n3. Jurnal")
            jenis = input("Nomor yang dipilih: ")
            
            kode = input("Masukkan Kode Koleksi: ")
            judul = input("Masukkan Judul: ")
            tahun = input("Masukkan Tahun Terbit: ")
            penerbit = input("Masukkan Penerbit: ")

            if jenis == '1':
                pengarang = input("Masukkan Pengarang: ")
                daftar_koleksi.append(Buku(kode, judul, tahun, penerbit, pengarang))
                print("Data berhasil ditambahkan")
            
            elif jenis == '2':
                edisi = input("Masukkan Edisi: ")
                daftar_koleksi.append(Majalah(kode, judul, tahun, penerbit, edisi))
                print("Data berhasil ditambahkan")
            
            elif jenis == '3':
                bidang = input("Masukkan Bidang Studi: ")
                impact = input("Masukkan Impact Factor: ")
                daftar_koleksi.append(Jurnal(kode, judul, tahun, penerbit, bidang, impact))
                print("Data berhasil ditambahkan")
            input("\nTekan [ENTER] untuk kembali ke menu")

        elif pilih == '2':
            kode_hapus = input("\nHAPUS DATA KOLEKSI\nMasukkan Kode Koleksi: ")
            
            ditemukan = False
            for k in daftar_koleksi:
                if k.kode == kode_hapus:
                    ditemukan = True
                    break
            
            if ditemukan:
                daftar_koleksi = [k for k in daftar_koleksi if k.kode != kode_hapus]
                print("Data sukses dihapus")
            else:
                print("Data tidak ditemukan")
                
            input("\nTekan [ENTER] untuk kembali ke menu")

        elif pilih == '3':
            print("\nDATA KOLEKSI")
            if not daftar_koleksi:
                print("Data masih kosong silahkan diisi dulu yaa... :)")
            for i, k in enumerate(daftar_koleksi, 1):
                print(f"\nKoleksi {i}:")
                print(k.info()) 
            input("\nTekan [ENTER] untuk kembali ke menu")

        elif pilih == '4':
            print("Terimakasih dan sampai jumpa :)")
            break
        
if __name__ == "__main__":
    menu()