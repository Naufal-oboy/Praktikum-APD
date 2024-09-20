nilai_tukar_usd = 0.000065
nilai_tukar_euro = 0.000059
nilai_tukar_yen = 0.0093


rupiah = float(input("Masukkan jumlah Rupiah: "))


dollar = rupiah * nilai_tukar_usd
euro = rupiah * nilai_tukar_euro
yen = rupiah * nilai_tukar_yen


print("Jumlah dalam Dollar Amerika : {:.2f} USD".format(dollar))
print("Jumlah dalam Euro          : {:.2f} Euro".format(euro))
print("Jumlah dalam Yen           : {:.2f} Yen".format(yen))
