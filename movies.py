import imdb
from imdb import Cinemagoer

ia = imdb.IMDb()
person = ia.get_person('0005132')
print(person['name'])

bottom = ia.get_bottom100_movies()
for movie in bottom:
    print(movie['title'])
