#input
tahun_lahir = int(input('Masukan tahun lahir Anda : '))
#kalkulasi
age_calculation = 2021 - tahun_lahir;
#age revealing
print("Usia kamu adalah ",age_calculation," tahun")
#category
# usia 0
# usia 1-3
# usia 4-5
# usia 6-12

#logic code
if(age_calculation == 0):
    print("Kamu belum boleh masuk sekolah")
if(age_calculation>=1) and (age_calculation<=3):
    print("Kamu sudah bisa masuk Toddler")
if(age_calculation == 4) or (age_calculation == 5):
    print("Kamu sudah bisa masuk TK")
if(age_calculation>=6) and (age_calculation<=12):
    print("Kamu sudah bisa masuk SD")
if(age_calculation>=13) and (age_calculation<=15):
    print("Kamu sudah SMP")
if(age_calculation>=16) and (age_calculation<=18):
    print("Kamu sudah SMA")
if(age_calculation>=19) and (age_calculation<=22):
    print("Kamu sudah kuliah S1")
if(age_calculation == 23) or (age_calculation == 24):
    print("Kamu sudah Lulus S1 dan mulai bekerja")
if(age_calculation>25):
    print("Kamu sedang lanjut S2 atau bekerja dengan giat")

    


    

