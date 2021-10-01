#program untuk memeriksa tinggi badan

tinggi = int(input('masukan angka tinggi badan kamu : '))

# kategori tinggi badan
# 1. Pendek : 100-150
# 2. Sedang : 151-165
# 3. Tinggi : 166-200
# 4. Tinggi sekali : 201-299
# 5. Raksasa : 300-399
# 6. Titan : lebih dari 1500



# pendek
if (tinggi>=100) and (tinggi<=150):
    print("Kamu cukup pendek")
# sedang 
if (tinggi>=151) and (tinggi<=165):
    print("Kamu cukup sedang")
# tinggi
if (tinggi>=166) and (tinggi<=200):
    print("Kamu cukup Tinggi")
# tinggi sekali
if (tinggi>=201) and (tinggi<=299):
    print("Kamu tinggi sekali")
# Raksasa
if (tinggi>=300) and (tinggi<=399):
    print("Kamu tinggi seperti raksasa")
# Titan
if (tinggi>=400) and (tinggi<=1500):
    print("Kamu tinggi sekali seperti Titan")
# undetected
if (tinggi>1500):
    print("Tinggi tidak terdeteksi")

    


