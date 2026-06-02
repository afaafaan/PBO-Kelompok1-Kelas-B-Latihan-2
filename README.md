# PBO-Kelompok1-Kelas-B-Latihan-2
Pembagian Tugas Kelompok (6 Orang)
1. Developer 1: (Abyan)
Tugas Utama: Mengatur repositori GitHub (membuat repo, mengelola project board atau issues, serta melakukan merge Pull Request).
Membuat file utama program (main.py) yang mengontrol alur menu utama (Pilihan 1-4) dan perulangan agar program bisa kembali ke menu utama menggunakan Tekan [ENTER].

2. Developer 2: (Dafa)
Core OOP Architect (Abstraction & Base Class)
Tugas Utama:
Merancang Abstract Base Class (kelas induk abstrak)
Menerapkan konsep Abstraksi menggunakan modul abc di Python (@abstractmethod).
Menentukan atribut bersama hasil identifikasi (Kode Koleksi, Judul, Tahun Terbit, Penerbit) dan metode abstrak yang harus dimiliki semua jenis koleksi (misal: tampil_info()).
Output File: koleksi_base.py

3. Developer 3: (Muzni)
Subclass Specialist - Buku & Majalah (Inheritance)
Tugas Utama:
Membuat kelas turunan (Inheritance) dari kelas utama untuk objek Buku dan Majalah.
Menambahkan atribut spesifik: Pengarang (untuk Buku) dan Edisi (untuk Majalah).
Mengimplementasikan Polimorfisme dengan melakukan override pada fungsi tampil_info() agar menampilkan data sesuai format tampilan di soal.
Output File: buku.py dan majalah.py

4. Developer 4: (Jihan)
Subclass Specialist - Jurnal
Tugas Utama:
Membuat kelas turunan untuk objek Jurnal dengan atribut spesifik (Bidang Studi dan Impact Factor).

5. Developer 5: (Faradilla)
QA, Database & CRUD Manager (Logic Handler)
Tugas Utama:
Membuat kelas pengelola data (LibraryManager) yang menyimpan list dari semua objek koleksi.
Membuat fungsi Tambah Data (menerima input objek koleksi apa saja berkat Polimorfisme).
Membuat fungsi Hapus Data berdasarkan Kode Koleksi.
Membuat fungsi Tampil Semua Data yang melakukan perulangan (looping) dan memanggil fungsi tampil_info() dari masing-masing objek secara polimorfis.
Melakukan Test/pengujian kode dan memeriksa kesalahan kode.
Output File: manager.py

6. Developer 6: (Niken)
Technical Writer (Tester & Documentation)
Tugas Utama:
Membuat kode test
