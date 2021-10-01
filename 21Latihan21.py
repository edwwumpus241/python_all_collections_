print("Welcome to grade convertor! recommended for teachers")
print("the instruction is enter the grade your student got and we will convert it to alphabet")
grade = int(input("Enter the grade : "))
if grade >100:
    print("Nilai melebihi batas. periksa kembali")
elif grade >= 90:
    print("Your student get an 'A' ")
elif grade > 79:
    print("Your student get a 'B' ")
elif grade > 69:
    print("Your student get a 'C' ")
elif grade > 64:
    print("Your student get a 'D' ")
else:
    print("Your student get a 'E' ")
    
