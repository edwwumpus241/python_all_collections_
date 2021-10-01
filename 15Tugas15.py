#input codes
buku_1 = int(input('masukan harga buku 1: '))
buku_2 = int(input('masukan harga buku 2: '))
buku_3 = int(input('masukan harga buku 3: '))
buku_4 = int(input('masukan harga buku 4: '))
buku_5 = int(input('masukan harga buku 5: '))
#total
total_harga_buku = buku_1 + buku_2 + buku_3 + buku_4 + buku_5;
diskon1 = total_harga_buku * 0.10
diskon2 = total_harga_buku * 0.25
diskon3 = total_harga_buku * 0.50
total_pembelian1 = total_harga_buku - diskon1;
total_pembelian2 = total_harga_buku - diskon2;
total_pembelian3 = total_harga_buku - diskon3;
print("total harga buku kamu",total_harga_buku)
#logic codes
if (total_harga_buku >= 199000) and (total_harga_buku<= 499000):
    print("Anda mendapatkan diskon sebesar 10%,yaitu ", diskon1)
    print("total pembelian kamu adalah ", total_pembelian1)
if (total_harga_buku >= 499000) and (total_harga_buku <= 999000):
    print("Anda mendapat diskon sebesar 25% ", diskon2)
    print("Total pembelian anda adalah ", total_pembelian2)
if total_harga_buku >= 999000:
    print("Anda mendapat diskon sebesar 50% ",diskon3)
    print("total pembelian anda adalah ", total_pembelian3)
if total_harga_buku <= 199000:
    print("kamu nggak dapat diskon")
    print("total harga buku anda adalah ", total_harga_buku)



   
    
    

