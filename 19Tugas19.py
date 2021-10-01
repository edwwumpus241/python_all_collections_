print("Hello welcome to this money changer program")
print("The list below are the banknotes we have currently")
print("Note: enter the ID to convert the banknote")
print("ID : 1 .Dollar to Rupiah")
print("ID : 2 .Euro to Rupiah")
print("ID : 3 .Ringgit to Rupiah")
print("ID : 4 .Yen to Rupiah")
print("ID : 5 .Won to Rupiah")
print("ID : 6 .Poundsterling to Rupiah")
print("ID : 7 .Rupee to Rupiah")
print("ID : 8 .Ruble to Rupiah")
print("Credit to Google(helps me to find the currency rate")
id_detecting = int(input("Enter one ID that has been shown in your screen : "))
amount_detecting = int(input("Enter the amount of the money to convert : "))
id_1 = 14000;
id_2 = 17000;
id_3 = 3000;
id_4 = 132.23;
id_5 = 1267;
id_6 = 20000;
id_7 = 194.21;
id_8 = 195.70;
if id_detecting == 1:
    converting = id_1 * amount_detecting;
    print(amount_detecting ,"Dollar in Rupiah are ",converting ," Rupiah")
if id_detecting == 2:
    converting_1 = id_2 * amount_detecting;
    print(amount_detecting ,"Euro in Rupiah are ",converting_1 ," Rupiah")
if id_detecting == 3:
    converting_2 = id_3 * amount_detecting;
    print(amount_detecting ,"Ringgit in Rupiah are ",converting_2 ," Rupiah")
if id_detecting == 4:
    converting_3 = id_4 * amount_detecting;
    print(amount_detecting ,"Yen in RUpiah are ",converting_3 ," Rupiah")
if id_detecting == 5:
    converting_4 = id_5 * amount_detecting;
    print(amount_detecting ,"Won in Rupiah are ",converting_4 ,"Rupiah")
if id_detecting == 6:
    converting_5 = id_6 * amount_detecting;
    print(amount_detecting ,"Poundsterling in Rupiah are ",converting_5 ," Rupiah")
if id_detecting == 7:
    converting_6 = id_7 * amount_detecting;
    print(amount_detecting ,"Rupee in Rupiah are ",converting_6 ," Rupiah")
if id_detecting == 8:
    converting_7 = id_8 * amount_detecting;
    print(amount_detecting ,"Ruble in Rupiah are ",converting_7 ," Rupiah")
if id_detecting <1:
    print("Chap, read the list again")
if id_detecting >8:
    print("Buckaroo, read the list again")
    
