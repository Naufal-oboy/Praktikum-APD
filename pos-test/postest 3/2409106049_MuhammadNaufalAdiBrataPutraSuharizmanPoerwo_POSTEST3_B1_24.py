import os
# Tampilan awal menu
print ("============================================================")
print (" Menu Program Pilihan Menghitung Luas/Keliling Bangun Datar ")
print ("============================================================")
print (" 1. Luas Segitiga ")
print (" 2. keliling Persegi")
print (" 3. Luas Persegi Panjang")
print (" 4. Keliling Lingkaran ")
print (" 5. Keluar Program")
print ("============================================================")

# Memasukkan input pilihan menu
menu = float (input ("Masukkan Nomor Pilihan Menu : "))

# Kondisi setiap menu yang dipilih
if menu == 1:
    alas =  float (input ("masukkan alas : "))
    tinggi = float (input ("masukkan tinggi : "))
    luas_segitiga =   (alas * tinggi /2)
    print ("Luas Segitiga : ", luas_segitiga, "cm")
elif menu == 2:
    sisi = float (input ("masukkan sisi : "))
    Keliling_Persegi =  (4 * sisi )
    print ("Keliling Persegi : ", Keliling_Persegi,"cm")
elif menu == 3:
    panjang = float (input("Masukkan Panjang : "))
    lebar = float (input ("Masukkan Lebar : "))
    Luas_Persegi_Panjang = panjang * lebar
    print (" Luas Persegi Panjang : ", Luas_Persegi_Panjang, "cm")
elif menu == 4:
    jari_jari = float (input ("Masukkan Jari-Jari : "))
    Keliling_Lingkaran = 2 * 22/7 * jari_jari
    print ("Keliling Lingkaran : ",  Keliling_Lingkaran, "cm")
elif menu == 5:
       os.system ("cls")
       print ("baiklah, sampai ketemu lagi")
else:
   print ("menu tidak tersedia, silahkan masukkan angka sesuai menu")