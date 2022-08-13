list1 = [1,2,3,4,5,]   #6 will be ignored if present

list2 =['one', 'two','three', 'four', 'five']

zipped = list(zip(list1,list2))

print(zipped)


unziped = list(zip(*zipped))
print(unziped)

for (l1 , l2) in zip(list1 , list2):
  print(l1)
  print(l2)
 

print()
print()
print()




items = ['apples', 'banana', 'orange']

count = [ 1,3,5]

price= [60,20,10]


for (l1,l2,l3) in zip(items , count, price):

 
  print(l1)
  print(l2)
  print(l3)
  
