# Panduan Input Data
print ('Panduan')
print ('+==== PILIHAN BENUA ====+')
print ('0. Asia')
print ('    11. Bahasa Indonesia')
print ('    12. Bahasa Mandarin')
print ('1. Amerika/Australia')
print ('    13. Bahasa Inggris')
print ('2. Eropa')
print ('    14. Bahasa Perancis')
print ('    15. Bahasa Spanyol')
print ('    16. Bahasa Italia')
print ('    17. Bahasa Rusia')
print ('+=======================+')

# Minta user ketikkan input data
benua = int(input('Pilihan Benua: '))
bahasa = int(input('Pilihan Bahasa: '))
nama = input('Ketikkan Nama Kamu: ')

# Benua Asia
if benua == 0 and bahasa == 11:
    print ('ini bahasa indonesia')
if benua == 0 and bahasa == 12:
    print ('ini bahasa mandarin')
# Ini antisipasi jika user input Benua 1 dan Bahasa selain 11 dan 12
if benua == 0 and bahasa < 11:
    print ('Pilihan bahasa tidak ada')
if benua == 0 and bahasa > 12:
    print ('Pilihan bahasa tidak ada')
    
# Benua Amerika
if benua == 1 and bahasa == 13:
    print ('ini bahasa inggris')
# Ini antisipasi jika user input Benua 2 dan Bahasa selain 21
if benua == 1 and bahasa < 13:
    print ('Pilihan bahasa tidak ada')
if benua == 1 and bahasa > 13:
    print ('Pilihan bahasa tidak ada')

# Benua Eropa
if benua == 2 and bahasa == 14:
    print ('ini bahasa perancis')
if benua == 2 and bahasa == 15:
    print ('ini bahasa spanyol')
if benua == 2 and bahasa == 16:
    print ('ini bahasa italia')
if benua == 2 and bahasa == 17:
    print ('ini bahasa rusia')
# Ini antisipasi jika user input Benua 3 dan Bahasa selain 31,32,33, dan 34
if benua == 2 and bahasa < 14:
    print ('Pilihan bahasa tidak ada')
if benua == 2 and bahasa > 17:
    print ('Pilihan bahasa tidak ada')

# Pilihan Benua diluar panduan
if benua > 2 :
    print ('Pilihan Benua dan Bahasa tidak ada. Baca lagi panduannya')
