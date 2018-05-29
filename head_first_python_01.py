movies = ["The Holy Grail",
          "The Life of Brian",
          "The Meaning of Life"]

print(movies[1])

cast = ["Cleese", "Palin", "Jones", "Idle"]
print(cast)
print(len(cast))
print(cast[1])

cast.append("Gilliam")
print(cast)

cast.pop()
print(cast)

cast.extend(["Gilliam", "Chapman"])
print(cast)

cast.remove("Chapman")
print(cast)

cast.insert(0, "Chapman")
print(cast)

movies.insert(1, 1975)
movies.insert(3, 1979)
movies.append(1983)
print(movies)


fav_movies = ["The Holy Grail", "The Life of Brian"]
print(fav_movies[0])
print(fav_movies[1])

for each_flick in fav_movies:
    print(each_flick)

count = 0
while count < len(movies):
    print(movies[count])
    count = count+1

for each_item in movies:
    print(each_item)
    
