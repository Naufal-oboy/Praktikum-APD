
import os
os.system('cls')

#login
kesempatan = 3

while kesempatan > 0:
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    if username == "naufal" and password == "049":
        print("Berhasil login")
        break
    else:
        print("Username atau password salah!")
        kesempatan -= 1
        print(f"Kesempatan login tersisa {kesempatan} kali")


# Tampilan awal menu
pilihan = "iya"
while pilihan == "iya":
    os.system('cls')
    print ("============================================================")
    print (" Menu Program Pilihan Menghitung Luas/Keliling Bangun Datar ")
    print ("============================================================")
    print (" 1. Luas Segitiga ")
    print (" 2. keliling Persegi")
    print (" 3. Luas Persegi Panjang")
    print (" 4. Keliling Lingkaran ")
    print (" 5. Keluar Program")
    print ("============================================================")
    
    menu = input("Masukkan Nomor Pilihan Menu : ")
    if menu in {"1", "2", "3", "4", "5"}:
        ulang = "iya"
    
        while ulang == "iya":
            
            if menu == "1":
                alas = float(input("Masukkan alas : "))
                tinggi = float(input("Masukkan tinggi : "))
                luas_segitiga = (alas * tinggi / 2)
                print("Luas Segitiga : ", luas_segitiga, "cm")
        
            elif menu == "2":
                sisi = float(input("Masukkan sisi : "))
                Keliling_Persegi = (4 * sisi)
                print("Keliling Persegi : ", Keliling_Persegi, "cm")
        
            elif menu == "3":
                panjang = float(input("Masukkan Panjang : "))
                lebar = float(input("Masukkan Lebar : "))
                Luas_Persegi_Panjang = panjang * lebar
                print("Luas Persegi Panjang : ", Luas_Persegi_Panjang, "cm")
        
            elif menu == "4":
                jari_jari = float(input("Masukkan Jari-Jari : "))
                Keliling_Lingkaran = 2 * 22 / 7 * jari_jari
                print("Keliling Lingkaran : ", Keliling_Lingkaran, "cm")

            ulang = input("Apakah ingin menghitung lagi ? (iya/tidak) : ")
            if ulang != "iya":
                break
    elif menu == "5":
        os.system("cls")
        print("Baiklah, sampai ketemu lagi")
        break    
    else:
        print("Menu tidak tersedia, silahkan masukkan angka sesuai menu")
        continue
            
