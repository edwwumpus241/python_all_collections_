comic_name = input('Enter comic name : ')
writter = input('Enter writter name : ')
artist = input('Enter artist name : ')
publication_date = int(input('Enter publication year : '))
main_characters = input('Enter main characters name : ')
info1 = 'Asterix, Asterix is a comic that comedy and satire genre, the first release comic name is Asterix The Gaul.'
info2 = ' Asterix comic was released in Pilote magazine, Rene goscinny he has written 5 bestselling comics. '
info3 = ' The story of Asterix comic is when the Romans rules in Galia there is one village that resist and amazingly beat the Romans because of their secret power made by Druid Panoramix. '
info4 = " And Asterix didn't travel alone, he travels with his big friend and very powerfull called 'Obelix' what made Obelix so powerfull is when Druid Panoramix done making his potion for the amazing strength Obelix fell to the cauldron. "
info_1_2 = info1 + info2;
info_3_4 = info3 + info4;
print('===========================================================')
print(comic_name.upper())
print('===========================================================')
print('')
print(info1.lower())
print('')
print(info2.lower())
print('')
print(info3.lower())
print('')
print(info4.lower())
print('information 1 has ', len(info1),' character')                       
print('information 2 has ', len(info2),' character')                       
print('information 3 has ', len(info3),' character')                       
print('information 4 has ', len(info4),' character')                       
print('informaton 1 to 2 has',len(info_1_2),'character')
print('informaton 3 to 4 has',len(info_3_4),'character')
print('All of the following information has ', len(info_1_2) + len(info_3_4) + len(info1) + len(info2) + len(info3) + len(info4),' character')
