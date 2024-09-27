# print ("perulangan ke-0")
# print ("perulangan ke-1")
# print ("perulangan ke-2")
# print ("perulangan ke-3")
# print ("perulangan ke-4")
# print ("perulangan ke-5")
# print ("perulangan ke-6")
# print ("perulangan ke-7")
# print ("perulangan ke-8")
# print ("perulangan ke-9")

# batas = 20
# for i in range(1,batas, 2):
#     print (f"perulangan ke-{i}")


# buah = ["apel", "mangga", "anggur"]
# for i in buah :
#     print (i)


# buah_banyak = ["apel", "mangga", "anggur"]
# for buah in buah_banyak :
#     print (buah)

# for baris in range (1,4):
#     print ("baris ke", baris)
#     for kolom in range (1,4):
#         print (kolom, "kolom" , end = "")
#     print()
#     print()


# lagi = "yes"
# ulang = 0
# while lagi == "yes":
#     ulang += 1
#     print ("mabar")
#     lagi = input ("mabar lagi gak?")
#     print ("selesai mabar")
#     print (f"perulanagan terjadi sebanyak {ulang} kali")

# for i in range (1,10):
#     if i == 4:
#         break
#     else:
#         print (f"perulangan ke-{i}")


# while True:
#     ulang = input("mabar lagi ? ")
#     if ulang == "tidak":
#         break
#     print ("mabar lagi")

# for i in range (1,10):
#     if i == 4:
#         continue
#     print (f"prulangan ke-{i}")

# print ("daftar bilangan ganjil dari 1-10")
# for i in range (10) :
#     if i % 2 == 0:
#         continue
#     print (i)

# print ("matrix")
# for i in range (5):
#     for j in range (5):
#         print ("*", end= "")
#     print()

# print ("segitiga siku-siku")
# for i in range (1,5):
#     print ("*" * i)

kesempatan = 3

while kesempatan > 0:
    username = input ("masukkan username: ")
    password = input ("masukkan password: ")

if username == "Admin" and password == "admin#1234":
    print ("berhasil login")
    breakpoint
else:
    print ("usename atau password salah !")
    kesempatan -= 1
    print ("kesempatan login sebanyak {kesempatan} kali")

print ("program utama")