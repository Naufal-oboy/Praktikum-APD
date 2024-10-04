# data = [1,2,3,4,True,[2,3],"adi"]
# data_2 = list ((1,2,3,4,5))
# data = ["apel","durian","jeruk"]
# print (data)
# print ()

# data [0] = "anggur"
# print (data)

# del data [2]
# print (data)

# print (len (data))
# print()
# data.extend (["rambutan","semangka"])
# print (data)
# print ()

# data.append("semangka")
# data.append (True)
# print (data)

# data.insert (0,"rambutan")
# print (data)

# print (data[6])
# # print (type (data_2))

# data.pop(1)
# print (data)

# nilai_hapus = data.pop(1)
# print (nilai_hapus)

# data_mahasiswa = [
#     ["060","ifnu",["Apd","orsikom"]],
#     ["065", "adi"]
#     ]

# print (data_mahasiswa [0][2][0])

# data_mahasiswa = [
#     ["admin","admin123","admin"]
#     ["user","user1234","user"]
# ]

# print (data_mahasiswa[0])

# buah = ["apel","durian","jeruk"]
# index = 1
# for data in buah :
#     print (f"data ke {index}")
#     print (data)
#     print ("="*10)
#     index = index + 1

# for index in range (len(buah)):
#     print (f"data ke {index + 1}")
#     print (buah[index])
#     print ("=" * 10)

# for index, item in enumerate(buah):
#     print (f"data ke {index + 1}")
#     print (item)

# for index, item in enumerate (len (data_mahasiswa):
#     print (f"data ke {index + 1}")
#     print (f"username :,{item[0]}")


# buah = ["apel","durian","jeruk"]
# buah1, *banyak_buah = buah
# print (buah1)
# print (banyak_buah)


import os
data_mahasiswa = ["ifnu","adi","ucup","michael"]

while True:
    print    ("menu")
    print ("1 >>> list data")
    print ("2 >>> tambah data")
    print ("3 >>> edit data")
    print ("4 >>> hapus data")
    print ("5 >>> keluar")
    
    menu = input ("masukkan pilihan menu >>>> ")
    os.system ("cls")

