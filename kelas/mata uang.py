nilai_tukar_usd = 0.000067
nilai_tukar_euro = 0.000062
nilai_tukar_yen = 0.007


rupiah = float(input("Masukkan jumlah Rupiah: "))


dollar = rupiah * nilai_tukar_usd
euro = rupiah * nilai_tukar_euro
yen = rupiah * nilai_tukar_yen


print("===============================")
print("         Hasil Konversi       ")
print("===============================")
print("Jumlah dalam Dollar Amerika : {:.2f} USD".format(dollar))
print("Jumlah dalam Euro          : {:.2f} Euro".format(euro))
print("Jumlah dalam Yen           : {:.2f} Yen".format(yen))
print("===============================")