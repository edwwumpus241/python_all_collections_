#Introduction
print("==================================================")
print("--------------------------------------------------")
print("Hallo tuan, ini adalah timeline anda untuk bersiap")
print("--------------------------------------------------")
print("==================================================")
#interactve code
jam = int(input("Ketikkan jam(hanya angkasaja, mis : 21) : "))
print("==================================================")
#good ol fashion of logic
if jam == 5 or jam == 6:
    print("=================================")
    print("Sedang siap-siap untuk ke sekolah")
    print("=================================")
elif jam >= 7 and jam <= 8:
    print("===============")
    print("Sedang belajar")
    print("===============")
elif jam == 9:
    print("=================")
    print("Istirahat pertama")
    print("=================")
elif jam >=10 and jam <11:
    print("==============")
    print("Sedang belajar")
    print("==============")
elif jam == 12:
    print("===============")
    print("Istirahat kedua")
    print("===============")
elif jam == 13 or jam == 14:
    print("===============")
    print("Sedang belajar")
    print("===============")
elif jam == 15:
    print("==============")
    print("Pulang sekolah")
    print("==============")
elif jam >= 16 and jam <= 19:
    print("==============================================")
    print("Lihat TV atau baca novel atau kegiatan lainnya")
    print("==============================================")
#else if the user randomly put numbers that are outbound
else :
    print("===========")
    print("Tidur malam")
    print("===========")
                  
    
