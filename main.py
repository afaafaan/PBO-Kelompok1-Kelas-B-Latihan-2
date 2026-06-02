from manager import LibraryManager
from koleksi import Buku, Majalah, Jurnal

def main():
    manager = LibraryManager()

    while True:
        print("=======================================")
        print("MENU PROGRAM")
        print("---------------------------------------")
        print("1. Tambah data koleksi")
        print("2. Hapus data koleksi")
        print("3. Tampil semua data koleksi")
        print("4. Keluar")
        print()
        
        pilihan = input("Nomor yang dipilih: ")

        if pilihan == "1":
            print("---------------------------------------")
            print("JENIS KOLEKSI YANG AKAN DITAMBAH")
            print()
            print("1. Buku")
            print("2. Majalah")
            print("3. Jurnal")
            print()
            jenis = input("Nomor yang dipilih: ")

            print("---------------------------------------")
            if jenis == "1":
                print("TAMBAH DATA BUKU")
                print()
                kode = input("Masukkan Kode Koleksi : ")
                judul = input("Masukkan Judul        : ")
                tahun = input("Masukkan Tahun Terbit : ")
                pengarang = input("Masukkan Pengarang    : ")
                penerbit = input("Masukkan Penerbit     : ")
                
                # Membuat objek dan memasukkannya ke database manager
                produk = Buku(kode, judul, tahun, penerbit, pengarang)
                manager.tambah_data(produk)
                print("---------------------------------------")
                print("Tambah Buku Sukses")

            elif jenis == "2":
                print("TAMBAH DATA MAJALAH")
                print()
                kode = input("Masukkan Kode Koleksi : ")
                judul = input("Masukkan Judul        : ")
                tahun = input("Masukkan Tahun Terbit : ")
                penerbit = input("Masukkan Penerbit     : ")
                edisi = input("Masukkan Edisi        : ")
                
                produk = Majalah(kode, judul, tahun, penerbit, edisi)
                manager.tambah_data(produk)
                print("---------------------------------------")
                print("Tambah Majalah Sukses")

            elif jenis == "3":
                print("TAMBAH DATA JURNAL")
                print()
                kode = input("Masukkan Kode Koleksi : ")
                judul = input("Masukkan Judul        : ")
                tahun = input("Masukkan Tahun Terbit : ")
                penerbit = input("Masukkan Penerbit     : ")
                bidang = input("Masukkan Bidang Studi : ")
                impact = input("Masukkan Impact Factor: ")
                
                produk = Jurnal(kode, judul, tahun, penerbit, bidang, impact)
                manager.tambah_data(produk)
                print("---------------------------------------")
                print("Tambah Jurnal Sukses")

            input("\nTekan [ENTER] untuk kembali ke menu program")

        elif pilihan == "2":
            print("---------------------------------------")
            print("HAPUS DATA KOLEKSI")
            print()
            kode = input("Masukkan Kode Koleksi : ")
            manager.hapus_data(kode)
            input("\nTekan [ENTER] untuk kembali ke menu program")

        elif pilihan == "3":
            manager.tampil_semua_data()
            input("Tekan [ENTER] untuk kembali ke menu program")

        elif pilihan == "4":
            print("Keluar dari program. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!")
            input("\nTekan [ENTER] untuk kembali ke menu program")

if _name_ == "_main_":
    main()
