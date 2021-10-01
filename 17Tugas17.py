#denda buku di perpustakaan
buku_denda1 = int(input("Masukan jumlah hari buku 1 : "))
buku_denda2 = int(input("Masukan jumlah hari buku 2 : "))
buku_denda3 = int(input("Masukan jumlah hari buku 3 : "))
buku_denda4 = int(input("Masukan jumlah hari buku 4 : "))
buku_denda5 = int(input("Masukan jumlah hari buku 5 : "))
total_hari = buku_denda1 + buku_denda2 + buku_denda3 + buku_denda4 + buku_denda5;
print("Total hari peminjaman buku kamu adalah ", total_hari)
if total_hari <=3:
    print("Kamu mengembalikan buku tepat waktu N I C E")
if total_hari >3 and total_hari <7:
    print("Kamu terkena denda sebesar = 10.000 dude Uncool")
if total_hari >=7 and total_hari <=10:
    print("Kamu terkena denda sebesar = 20.000 dude that's uncool")
if total_hari >10 and total_hari <=20:
    print("Kamu terkena denda sebesar = 50.000 dude that's seriously uncool")
if total_hari >20:
    print("Kamu terkena denda sebesar = 200.000 dude that's very uncool dont go here again")
    
