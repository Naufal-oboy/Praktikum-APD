import os

akun = {
    "admin": {"role": "admin", "password": "admin123"}
}

jadwal_olahraga = {}

while True:
    os.system("cls")
    print("=============================")
    print("        daftar menu          ")
    print("=============================")
    print("1. Register")
    print("2. Login")
    print("3. Keluar")
    print("=============================")

    menu = input("Masukkan pilihan : ")

    if menu == "1": 
        os.system("cls")
        username = input("Masukkan username : ")
        password = input("Masukkan password : ")
        password_confirm = input("Masukkan ulang password : ")

        if password == password_confirm:
            akun[username] = {"role": "user", "password": password}
            print("Pendaftaran berhasil")
        else:
            print("Password tidak sama")
        input("Enter untuk melanjutkan...")

    elif menu == "2": 
        os.system("cls") 
        username = input("Masukkan username : ")
        password = input("Masukkan password : ")

        if username in akun and akun[username]["password"] == password:
            print(f"Selamat datang, {username}")
            
            if akun[username]["role"] == "admin":
                while True:
                    os.system("cls")
                    print("====================================")
                    print("      Daftar Jadwal Kegiatan        ")
                    print("====================================")
                    print("1. Lihat Jadwal Kegiatan Olahraga")
                    print("2. Tambah Jadwal Kegiatan Olahraga")
                    print("3. Ubah Jadwal Kegiatan Olahraga")
                    print("4. Hapus Jadwal Kegiatan Olahraga")
                    print("5. Keluar")
                    print("====================================")

                    menu_admin = input("Masukkan pilihan : ")

                    if menu_admin == "1":
                        os.system("cls")
                        if jadwal_olahraga:
                            for key, jadwal in jadwal_olahraga.items():
                                print("================================")
                                print(f"ID Jadwal : {key}")
                                print(f"Kegiatan : {jadwal['kegiatan']}")
                                print(f"Tanggal : {jadwal['tanggal']}")
                                print(f"Waktu : {jadwal['waktu']}")
                                print(f"Tempat : {jadwal['tempat']}")
                                print("================================")
                            input("Enter untuk melanjutkan...")
                        else:
                            print("Belum ada jadwal kegiatan")
                            input("Enter untuk melanjutkan...")

                    elif menu_admin == "2":
                        os.system("cls")
                        id_jadwal = input("Masukkan ID jadwal : ")
                        kegiatan = input("Masukkan jadwal kegiatan : ")
                        tanggal = input("Masukkan jadwal tanggal : ")
                        waktu = input("Masukkan waktu : ")
                        tempat = input("Masukkan lokasi tempat : ")

                        jadwal_olahraga[id_jadwal] = {
                            "kegiatan": kegiatan, 
                            "tanggal": tanggal, 
                            "waktu": waktu, 
                            "tempat": tempat
                        }
                        print("Jadwal kegiatan berhasil ditambahkan")
                        input("Enter untuk melanjutkan...")

                    elif menu_admin == "3":
                        os.system("cls")
                        if jadwal_olahraga:
                            for key, jadwal in jadwal_olahraga.items():
                                print("================================")
                                print(f"ID Jadwal : {key}")
                                print(f"Kegiatan : {jadwal['kegiatan']}")
                                print(f"Tanggal : {jadwal['tanggal']}")
                                print(f"Waktu : {jadwal['waktu']}")
                                print(f"Tempat : {jadwal['tempat']}")
                                print("================================")
                            
                            id_jadwal = input("Masukkan ID jadwal yang ingin diubah: ")
                            if id_jadwal in jadwal_olahraga:
                                kegiatan_baru = input("Masukkan kegiatan baru: ")
                                tanggal_baru = input("Masukkan tanggal baru: ")
                                waktu_baru = input("Masukkan waktu baru: ")
                                tempat_baru = input("Masukkan tempat baru: ")

                                jadwal_olahraga[id_jadwal] = {
                                    "kegiatan": kegiatan_baru, 
                                    "tanggal": tanggal_baru, 
                                    "waktu": waktu_baru, 
                                    "tempat": tempat_baru
                                }
                                print("Jadwal berhasil diubah")
                            else:
                                print("ID jadwal tidak valid")
                            input("Enter untuk melanjutkan...")
                        else:
                            print("Belum ada jadwal yang dapat diubah")
                            input("Enter untuk melanjutkan...")

                    elif menu_admin == "4":
                        os.system("cls")
                        if jadwal_olahraga:
                            for key, jadwal in jadwal_olahraga.items():
                                print("================================")
                                print(f"ID Jadwal : {key}")
                                print(f"Kegiatan : {jadwal['kegiatan']}")
                                print(f"Tanggal : {jadwal['tanggal']}")
                                print(f"Waktu : {jadwal['waktu']}")
                                print(f"Tempat : {jadwal['tempat']}")
                                print("================================")
                            
                            id_jadwal = input("Masukkan ID jadwal yang ingin dihapus: ")
                            if id_jadwal in jadwal_olahraga:
                                del jadwal_olahraga[id_jadwal]
                                print("Jadwal berhasil dihapus")
                            else:
                                print("ID jadwal tidak valid")
                            input("Enter untuk melanjutkan...")
                        else:
                            print("Belum ada jadwal yang dapat dihapus")
                            input("Enter untuk melanjutkan...")

                    elif menu_admin == "5":
                        print("Terima kasih, sampai jumpa kembali")
                        break

                    else:
                        print("Menu tidak tersedia")
                        input("Enter untuk melanjutkan...")

            else:
                while True:
                    os.system("cls")
                    print("====================================")
                    print("      Daftar Jadwal Kegiatan        ")
                    print("====================================")
                    print("1. Lihat Jadwal Kegiatan Olahraga")
                    print("5. Keluar")
                    print("====================================")

                    menu_user = input("Masukkan pilihan : ")

                    if menu_user == "1":
                        os.system("cls")
                        if jadwal_olahraga:
                            for key, jadwal in jadwal_olahraga.items():
                                print("================================")
                                print(f"ID Jadwal : {key}")
                                print(f"Kegiatan : {jadwal['kegiatan']}")
                                print(f"Tanggal : {jadwal['tanggal']}")
                                print(f"Waktu : {jadwal['waktu']}")
                                print(f"Tempat : {jadwal['tempat']}")
                                print("================================")
                            input("Enter untuk melanjutkan...")
                        else:
                            print("Belum ada jadwal kegiatan")
                            input("Enter untuk melanjutkan...")

                    elif menu_user == "5":
                        print("Terima kasih, sampai jumpa kembali")
                        break

                    else:
                        print("Menu yang anda pilih tidak tersedia")
                        input("Enter untuk melanjutkan...")

        else:
            print("Username atau password salah!")
            input("Enter untuk melanjutkan...")

    elif menu == "3": 
        os.system("cls")
        print("Terima kasih, sampai jumpa kembali")
        break

    else:
        print("Menu yang anda pilih tidak tersedia")
        input("Enter untuk melanjutkan...")
