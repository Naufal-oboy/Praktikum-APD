# input biodata
nama = str (input ("nama anda: "))
jurusan = str (input ("jurusan : "))
umur = int (input  ("umur : "))
agama = str (input ("agama : "))
tinggi_badan = float (input ("tinggi badan : "))
hobi = str (input ("hobi : "))
asal_sekolah = str (input ( "asal sekolah : "))
jenis_kelamin = str(input ("jenis kelamin (laki-Laki/perempuan): "))
total_variabel = umur + tinggi_badan

# check jenis kelamin
if jenis_kelamin == "laki-laki" or jenis_kelamin == "perempuan":
    gender = bool (True)
else:
    gender = bool (False)


# ouput biodata
print ("===============================")
print ("         Bio data Anda        ")
print ("===============================")
print ("Nama          : ",nama)
print ("Jurusan       : ",jurusan) 
print ("Agama         : ",agama)
print ("Umur          : ", umur, "tahun")
print ("Tinggi Badan  : ", tinggi_badan, "cm")
print ("Hobi          : ", hobi)
print ("Asal sekolah  : ", asal_sekolah)

if gender:
    print ("Jenis kelamin : ", jenis_kelamin)
else:
    print("Jenis Kelamin : tidak terdeteksi")

print("===============================")

print ("total variabel : ", total_variabel)