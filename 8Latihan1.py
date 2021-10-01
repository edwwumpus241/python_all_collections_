#Base code
film = input('Enter movie name: ')
director = input('Enter director name: ')
writter = input('Enter writter name: ')
main_character = input('Enter main character name: ')
actor = input('Enter actor name: ')
release_date = int(input('Enter movie release date: '))
budget = int(input('Enter movie budget: '))
movie_age = 2021 - release_date;
rupiah_budget = budget * 14600;
#Code result
print('===========================')
print("")
print('MOVIE : ', film)
print('')
print('===========================')
print('About ', film)
print("The ", film ,"main character name is ", main_character ," the performer is  " , actor)
print("The budget is about ", budget ,"and the director is ", director)
print("Realese date of the movie is ", release_date ," and the age of the movie are ", movie_age ," year old")
print("The creator of this movie is ", writter)
print("The budget of this movie in Rupiah is ", rupiah_budget)
print("===========================")
