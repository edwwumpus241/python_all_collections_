kota = input('Nama Kota : ')

info1 = 'Kota Malang adalah sebuah kota yang terletak di Provinsi Jawa Timur, Indonesia.'
info2 = 'Kota Malang merupakan kota terbesar kedua di Jawa Timur setelah Surabaya.'
info3 = 'Kota ini terletak di dataran tinggi seluas 145,28 kilometer persegi yang terletak di tengah-tengah Kabupaten Malang'
info4 = 'Bersama dengan Kota Batu dan Kabupaten Malang, Kota Malang merupakan bagian dari kesatuan dari kesatuan wilayah yang dikenal dengan Malang.'

total_karakter = len(info1) + len(info2) + len(info3) + len(info4)

print('=============================')
print(kota.upper())
print('=============================')
print('')
print('Informasi: ')
print(info1, info2, info3, info4)
print('')
print ('panjang informasi 1 = ', len(info1), 'karakter')
print ('panjang informasi 2 = ', len(info2), 'karakter')
print ('panjang informasi 3 = ', len(info3), 'karakter')
print ('panjang informasi 4 = ', len(info4), 'karakter')

print('Panjang total informasi = ', total_karakter, 'karakter')

