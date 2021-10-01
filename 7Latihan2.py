nama_permainan = input('Nama permainan: ');
perusahaan_pengembang = input('Perusahaan/pengembang: ');
desainer_programmer = input('Desainer/Programmer: ');
negara_asal = input('Negara asal: ');
genre = input('Genre: ');
tahun_rilis = int(input('Tahun rilis: '));
grafik = input('Grafik: ');
usia_game = 2021 - tahun_rilis;

print("==========================")
print("nama game: ", nama_permainan)
print("")
print("==========================")
print("--------------------------")
print("Development")
print("==========================")
print("")
print("Perusahaan dan pengembang game tersebut adalah ", perusahaan_pengembang ," dan game ini di program dan di desain oleh  ", desainer_programmer)
print("Game ini dibuat di negara ", negara_asal)
print("Dan game ini dirilis tahun ", tahun_rilis ," pada hari ini game tersebut berusia ", usia_game)
print("")
print("==========================")
print("Gameplay")
print("==========================")
print(nama_permainan, "adalah ber genre ",genre ,"dan digame itu anda dapat memilih karakter-karakter yang ada di fim star wars")
print("")
print("Grafik game tersebut adalah: ", grafik)
print("==========================")
print("COMPANY")
print("Perusahaan yang membuat game ini bernama ", perusahaan_pengembang ," dan perusahaan ini berasal dari negara ", negara_asal)
