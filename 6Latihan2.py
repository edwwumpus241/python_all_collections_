age_now = int(input('Masukkan usia anda :'))
age_next_year = age_now + 1

birth_year = int(input('Masukkan tahun :'))
year = int(input('Masukkan tahun yang dituju :'))
age = year - birth_year

person1_birthyear = int(input('Masukkan tanggal lahir orang 1 :'))
person2_birthyear = int(input('Masukkan tanggal lahir orang 2 :'))

result_subject1 = person1_birthyear - person2_birthyear

print('Pada ulang tahun anda berikutnya, usia anda', age_next_year)
print('Umur anda pada tahun ' +str(year) + ' adalah ' +str(age))
print('Selisih umur orang 2 dan orang 1 adalah :' ,result_subject1)
