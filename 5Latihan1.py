remote_tv = 2
laptop = 1
hand_phone = 1
baygon = 1
sofa = 3
tv = 1
vacuum = 1
jam_tangan = 1
barang_elektronik = remote_tv + laptop + tv + vacuum + hand_phone;
barang_nonelektronik =  baygon + sofa + jam_tangan;
total_barang = barang_elektronik + barang_nonelektronik
print("==========================================================")
print("Saya mempunyai remote tv yang jumlahnya " + str (remote_tv))
print("Saya mempunyai laptop yang jumlah " + str (laptop))
print("Saya juga mempunyai barang yang jumlahnya sama seperti laptop " + str (hand_phone))
print("Saya juga mempunyai barang yang berjumlah satu yaitu " + str (baygon))
print("Saya mempunyai sofa yang berjumlah " + str (sofa))
print("Saya mempunyai tv yang berjumlah " + str (tv))
print("Saya juga mempunyai vacuum yang berjumlah " + str (vacuum))
print("Saya juga mempunyai jam tangan yang berjumlah " + str (jam_tangan))
print("Total barang elektronik yang disekitar saya adalah " + str (barang_elektronik))
print("Total barang non elektronik yang disekitar saya adalah " + str (barang_nonelektronik))
print("Total semua barang dari barang non elektronik sampai eletronik adalah " + str (total_barang))
print("==========================================================")
