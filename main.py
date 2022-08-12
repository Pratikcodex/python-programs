#list comprehension

names = ['jennifer', 'raj' ,'pratik', ]
l = []
for person in names:
  print([person for person in names])

  l=[]
  
  for person in names:
    
    
    l.append(person+'dumped me')
    
    print(l)

print([person +'dumped me' for person in names])


#runnning comprehension inside a dictionary

movies_and_rating = {"interstellar":10 , "dark knight":9 ,"teen wolf":8 , "ek vilain":5, "bharamhastra":4 , "50 shades":2 }

l = []

for movie in movies_and_rating:
  if movies_and_rating[movie] > 6:
    l.append(movie)
    print(l)

print([movie for movie in movies_and_rating if movies_and_rating[movie] > 6 ])
