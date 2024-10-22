import os

akun = {
    "admin": {"role": "admin", "password": "admin123"}
}

jadwal_olahraga = {}

def lihat_jadwal():
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

def tambah_jadwal():
    id_jadwal = input("Masukkan ID jadwal : ")
    if id_jadwal in jadwal_olahraga:
        print ("ID jadwal sudah ada")
        return tambah_jadwal()
    
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
    return {
        "ID Jadwal": id_jadwal,
        "Kegiatan": kegiatan,
        "Tanggal": tanggal,
        "Waktu": waktu,
        "Tempat": tempat
    }

def ubah_jadwal():
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
            input("Enter untuk melanjutkan...")
            return {
            "kegiatan": kegiatan_baru, 
            "tanggal": tanggal_baru, 
            "waktu": waktu_baru, 
            "tempat": tempat_baru
            }
        else:
            print("ID jadwal tidak valid")
            input("Enter untuk melanjutkan...")
            return "ID jadwal tidak valid"
    else:
        print("Belum ada jadwal yang dapat diubah")
        input("Enter untuk melanjutkan...")
        return "Belum ada jadwal yang dapat diubah"

def hapus_jadwal():
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
            input("Enter untuk melanjutkan...")
            return "Jadwal berhasil dihapus"
        else:
            print("ID jadwal tidak valid")
            input("Enter untuk melanjutkan...")
            return "ID jadwal tidak valid"
    else:
            print("Belum ada jadwal yang dapat dihapus")
            input("Enter untuk melanjutkan...")
            return "Belum ada jadwal yang dapat dihapus"

def membersihkan_layar():
    os.system("cls")

def menu_utama():
    print("=============================")
    print("        daftar menu          ")
    print("=============================")
    print("1. Register")
    print("2. Login")
    print("3. Keluar")
    print("=============================")

    menu = input("Masukkan pilihan : ")
    return menu

def admin_menu():
    while True:
        membersihkan_layar()
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
            membersihkan_layar()
            lihat_jadwal()

        elif menu_admin == "2":
            membersihkan_layar()
            hasil_tambah= tambah_jadwal()
            print (hasil_tambah)

        elif menu_admin == "3":
            membersihkan_layar()
            hasil_ubah = ubah_jadwal()
            print (hasil_ubah)

        elif menu_admin == "4":
            membersihkan_layar()
            hasil_hapus = hapus_jadwal()
            print (hasil_hapus)

        elif menu_admin == "5":
            return 

        else:
            print("Menu tidak tersedia")
            input("Enter untuk melanjutkan...")
            

def user_menu ():
    while True:
        membersihkan_layar()
        print("====================================")
        print("      Daftar Jadwal Kegiatan        ")
        print("====================================")
        print("1. Lihat Jadwal Kegiatan Olahraga")
        print("5. Keluar")
        print("====================================")

        menu_user = input("Masukkan pilihan : ")

        if menu_user == "1":
            membersihkan_layar()
            lihat_jadwal()

        elif menu_user == "5":
            return

        else:
            print("Menu yang anda pilih tidak tersedia")
            input("Enter untuk melanjutkan...")


while True:
    membersihkan_layar()
    menu = menu_utama()

    if menu == "1": 
        membersihkan_layar()
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
        membersihkan_layar() 
        username = input("Masukkan username : ")
        password = input("Masukkan password : ")

        if username in akun and akun[username]["password"] == password:
            print(f"Selamat datang, {username}")
            
            if akun[username]["role"] == "admin":
                admin_menu()

            else:
                user_menu()

        else:
            print("Username atau password salah!")
            input("Enter untuk melanjutkan...")

    elif menu == "3": 
        membersihkan_layar()
        print("Terima kasih, sampai jumpa kembali")
        break

    else:
        print("Menu yang anda pilih tidak tersedia")
        input("Enter untuk melanjutkan...")
