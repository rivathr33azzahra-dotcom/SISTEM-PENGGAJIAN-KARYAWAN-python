from manager import Manager
from supervisor import Supervisor
from staff import Staff

daftar_karyawan = []

while True:
    print("\n=== SISTEM PENGGAJIAN KARYAWAN ===")
    print("1. Tambah Karyawan")
    print("2. Lihat Data")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":

        nama = input("Nama : ")
        nip = input("NIP  : ")

        print("\nJabatan")
        print("1. Manager")
        print("2. Supervisor")
        print("3. Staff")

        jabatan = input("Pilih jabatan: ")

        if jabatan == "1":
            karyawan = Manager(nama, nip)

        elif jabatan == "2":
            karyawan = Supervisor(nama, nip)

        elif jabatan == "3":
            karyawan = Staff(nama, nip)

        else:
            print("Jabatan tidak valid")
            continue

        daftar_karyawan.append(karyawan)
        print("Data berhasil ditambahkan!")

    elif pilihan == "2":

        print("\n=== DATA KARYAWAN ===")

        for k in daftar_karyawan:
            print("-------------------")
            print("Nama :", k.get_nama())
            print("NIP  :", k.get_nip())
            print("Gaji :", f"Rp{k.hitung_gaji():,}")

    elif pilihan == "3":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")