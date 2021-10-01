#Guide book for user

print("panduan")
print("================================")
print("0 adalah benua Asia")
print("==========================")
print("5 adalah Bahasa Indonesia")
print("6 adalah bahasa Mandarin")
print("7 adalah bahasa Vietnam")
print("================================")
print("1 adalah benua Amerika")
print("================================")
print("8 adalah Inggris")
print("================================")
print("2 adalah benua Eropa")
print("================================")
print("9 adalah Perancis")
print("10 adalah bahasa Spanyol atau Espana")
print("11 adalah bahasa Russia")
print("12 adalah bahasa German")
print("13 adalah bahasa Italia")
print("14 adalah bahasa Finlandia")
print("15 adalah bahasa Belanda/Netherlands")
print("================================")
print("3 adalah benua Afrika")
print("================================")
print("16 adalah bahasa afrikaans")
print("17 adalah bahasa xhosa")
print("18 adalah bahasa swahili")
print("================================")

#Logic codes for continent
continent = int(input("Masukan Benua : "))
languange = int(input("Masukan bahasa(baca panduan): "))
name = input("Masukan nama anda: ")
#Asia
if continent == 0 and languange == 5:
    print("Halo ", name," selamat belajar pemrograman Python!")
if continent == 0 and languange == 6:
    print("Ni hao ", name, " kuai xuexi python")
if continent == 0 and languange == 7:
    print("xin chao ", name, " chuc mot ngay tot lanh khi hoc python")
if continent == 0 and languange <5:
    print("bAcA pAnDuAn LaGi")
if continent == 0 and languange >7:
    print("bAcA pAnDuAn LaGi")
#America/Oceania
if continent == 1 and languange == 8:
    print("Hello ", name," have a good day learning Python!")
if continent == 1 and languange >8:
    print("bAcA pAnDuAn LaGi")
if continent == 1 and languange <8:
    print("bAcA pAnDuAn LaGi")
#Eropa
if continent == 2 and languange == 9:
    print("Bonjour ", name," heureux d'apprendre le python")
if continent == 2 and languange == 10:
    print("Hola ", name, " feliz aprendizaje, piton")
if continent == 2 and languange == 11:
    print("Privet ", name," zhelayu udachnogo izucheniya programmirovaniya na Python")
if continent == 2 and languange == 12:
    print("hallo, ", name, " viel spab beim python lernen")
if continent == 2 and languange == 13:
    print("Ciao ", name," buon apprendimito della programmazione Python")
if continent == 2 and languange == 14:
    print("Hei ", name, "hyvaa paivaa pythonin oppimisessa")
if continent == 2 and languange == 15:
    print("Hallo", name, "fijne dag om python te leren")
if continent == 2 and languange <9:
    print("bAcA pAnDuAn LaGi")
if continent == 2 and languange >15:
    print("bAcA pAnDuAn LaGi")
#Afrika
if continent == 3 and languange == 16:
    print("hallo ", name, " 'n goeie dag om luislang te leer")
if continent == 3 and languange == 17:
    print("molo ", name, " ube nosuku olumnandi lokufunda ipython")
if continent == 3 and languange == 18:
    print("hello ", name, " uwe na siku njema ya kujifunza chatu")
if continent == 3 and languange <16:
    print("bAcA pAnDuAn LaGi")
if continent == 3 and languange >18:
    print("bAcA pAnDuAn LaGi")
    
if continent >3:
    print(" B A C A   P A N D U A N ", name)


