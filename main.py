library_1 ={'harry', 'game of thrones', 'potter'}

library_2 = {'harry', 'hola'}

all_books_in_town = library_1.union(library_2)

same_books_in_town=library_1.intersection(library_2)

print(all_books_in_town)#union

print()

print(same_books_in_town)#intersection


print()

#difference

diff = library_1.difference(library_2)
diff2 = library_2.difference(library_1)
print(diff)
print()
print(diff2)

