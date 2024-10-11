data_mhs = {
    "nama": "ucup",
    "nim" : 1,
    "matkul" : ["kalkulus","jarkom","apd"],
    "dosen" : {
        "nama" : "pak awang",
        "matkul" : "apd"
    }
}
print (data_mhs["dosen"]["nama"])
# cache = data_mhs.pop("nim")

# # data_mhs["nama"] = "michael"
# # data_mhs["alamat"] = "Samarinda"
# # data_mhs["alamat"] = "tenggarong"

# # data_mhs.update({"alamat" : "samarinda"})
# # data_mhs.update({"alamat" : "tenggarong"})

# # for data in data_mhs:
# #     print(data)

# # for key_data, value_data in data_mhs.items():
# #     print(f"key: {key_data})

# # print (data_mhs.get("mapel", "gak ada"))
# # print (data_mhs["nama"])
# # print (data_mhs["nim"])
# print (data_mhs, "dictionary")
# print (cache, "cache")

# data_mhs ["id"] = cache
# print (data_mhs)

# # print (data_mhs.clear(), "clear")

# print (len(data_mhs))

# key = "apel", "jeruk", "mangga", "semangka","anggur"
# value = 1
# buah = dict.fromkeys(key, value)
# print (buah)

# for value in data_mhs:
#     print (data_mhs[value])

# for key in data_mhs:
#     print (data_mhs[key])

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }
# #menggunakan keys
# for i in Nilai.keys():
#     print(i)
#     print("")
# #menggunakan value
# for i in Nilai.values():
#     print(i)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)