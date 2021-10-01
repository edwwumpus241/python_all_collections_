print("Hello welcome and what do you want me to convert?")
print("this are the list of the banknotes we have currently")
print("Enter the ID to convert ya money")
print("ID : 1. Rupiah to Dollar")
print("ID : 2. Rupiah to Euro")
print("ID : 3. Rupiah to Ringgit")
print("ID : 4. Rupiah to Yen(japan)")
print("ID : 5. Rupiah to Won(south not north lmao")
print("ID : 6. Rupiah to poundsterling")
print("ID : 7. Rupiah to Rupee")
print("ID : 8. Rupiah to Ruble")
id_ = int(input("Enter one ID that has been shown in your screen : "))
amount_ = int(input("Enter the amount : "))
id_1 = 0.000069;
id_2 = 0.000059;
id_3 = 0.00029;
id_4 = 0.0076;
id_5 = 0.079;
id_6 = 0.000050;
id_7 = 195;
id_8 = 196;
id_9 = 0.0051;
id_10 = 14475;
if id_ <1:
    print("read the list senor")
if id_ == 1:
    convertor_1 = id_1 * amount_;
    print(amount_ ," Rupiah in Dollar are ",convertor_1 ," Dollar")
if id_ == 2:
    convertor_2 = id_2 * amount_;
    print(amount_ ," Rupiah in Euro are ",convertor_2 ," Euro")
if id_ == 3:
    convertor_3 = id_3 * amount_;
    print(amount_ ," Rupiah in Ringgit are ",convertor_3 ," Ringgit")
if id_ == 4:
    convertor_4 = id_4 * amount_;
    print(amount_ ," Rupiah in Yen are ",convertor_4," Yen")
if id_ == 5:
    convertor_5 = id_5 * amount_;
    print(amount_ ," Rupiah in Won are ",convertor_5 ," Won")
if id_ == 6:
    convertor_6 = id_6 * amount_;
    print(amount_ ," Rupiah in Poundsterling are ",convertor_6 ," Poundsterling")
if id_ == 7:
    convertor_7 =  amount_ / id_7;
    print(amount_ ," Rupiah in Rupee are ",convertor_7 ," Rupee")
if id_ == 8:
    convertor_8 = amount_ / id_8;
    print(amount_ ," Rupiah in Ruble are ",convertor_8 ," Ruble")
if id_ == 9:
    convertor_9 = id_9 * amount_;
    print(amount_ ," Rupiah in Ruble are ",convertor_9 ," Ruble")
if id_ == 10:
    convertor_10 = amount_ / id_10;
    print(amount_ ," Rupiah in Dollar are ",convertor_10 ," Dollar")
    
if id_ >10:
    print("read the list again ")














