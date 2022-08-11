#dictionaries in python 

groceries={'bananas':5 , 'apples':3}

contacts = {'john':65465464, 
           "jenny":{'phone':'1234141','email':'ea@gmail.com'}
           }


print(groceries['bananas'])

print()

print(groceries.get('apples'))

print()

print(contacts['jenny'])


sentence ="I Like the word pratik pratik is a good coder"

word_count ={
'I':1,
'pratik': 2
}

print(word_count)
word_count['Like']=1
print(word_count)


#dict.items()
print(word_count.items())
print()

#dict.keys
print(word_count.keys())
print()

#dict.values\
print()
print(word_count.values())
print()

#delete something from dictionary\
#dict.pop(key)

print(word_count)
print()
print(word_count.pop('I'))
print(word_count)

print()

#dict.popitem()delet the last one or the highest 

print(word_count)
print(word_count.popitem())
print(word_count)

print()


#dict.clear
#word_count.clear()










