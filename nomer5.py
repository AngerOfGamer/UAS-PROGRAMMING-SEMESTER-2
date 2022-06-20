from prettytable import PrettyTable
import mysql.connector

koneksi = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="programming"
)

active = True

while active:
    programming = koneksi.cursor()

    programming.execute('select*from mahasiswa')

    data = programming.fetchall()
    r = PrettyTable(['id', 'nama', 'nim'])

    for row in data:
        r.add_row(row)
    print(r)

    print("Pilih Aksi : ")
    print("1. Tambah Data")
    print("2. Update Data")
    print("3. Delete Data")
    print("4. Exit")
    inputUser = input("\nMasukkan Pilihan : ")

    if inputUser == '1':
        nama = input("Masukkan Nama : ")
        nim = input("Masukkan NIM  : ")

        if len(nama) == 0 and len(nim) == 0:
            print("Data Kosong")
        else:
            koneksiTest = koneksi.cursor()

            koneksiTest.execute(
                "insert into mahasiswa (nama, nim) VALUES (%s, %s)", (nama, nim))

            koneksi.commit()

            print("Data Berhasil Ditambahkan")
        cek = input("Apakah Anda Ingin Melanjutkan Program? (Ya/No) :")
        if cek == 'No':
            active = False
    if inputUser == '2':
        idUpdate = input("Masukkan Id yang ingin di update : ")
        print("Pilih tabel yang ingin diupdate : ")
        print("1. Nama")
        print("2. NIM")
        print("3. Ubah Seluruhnya")
        aksiUpdate = input("Pilih 1-3 : ")
        if aksiUpdate == '1':
            namaUpdate = input("Masukkan Nama Baru : ")
            koneksiTest = koneksi.cursor()
            koneksiTest.execute(
                f"update mahasiswa set nama = '{namaUpdate}' where id = '{idUpdate}'")
            koneksi.commit()
            print("Data Nama Berhasil Diupdate")
        elif aksiUpdate == '2':
            nimUpdate = input("Masukkan NIM Baru : ")
            koneksiTest = koneksi.cursor()
            koneksiTest.execute(
                f"update mahasiswa set nim = '{nimUpdate}' where id = '{idUpdate}'")
            koneksi.commit()
            print("Data NIM Berhasil Diupdate")
        elif aksiUpdate == '3':
            namaUpdate = input("Masukkan Nama Baru : ")
            nimUpdate = input("Masukkan NIM Baru : ")
            koneksiTest = koneksi.cursor()
            koneksiTest.execute(
                f"update mahasiswa set nama = '{namaUpdate}', nim = '{nimUpdate}' where id = '{idUpdate}'")
            koneksi.commit()
            print("Data Berhasil Diupdate")
        else:
            print("Masukkan 1-3")

        cek = input("Apakah Anda Ingin Melanjutkan Program? (Ya/No) : ")
        if cek == 'No':
            active = False
    if inputUser == '3':
        iddelete = input("Masukkan ID yang ingin di hapus : ")
        koneksiTest = koneksi.cursor()
        koneksiTest.execute(
            f"delete from mahasiswa where id='{iddelete}'")
        koneksi.commit()
        print("Data Berhasil Dihapus")
        cek = input("Apakah Anda Ingin Melanjutkan Program? (Ya/No) : ")
        if cek == 'No':
            active = False
    if inputUser == '4':
        active = False
