#using variables with for loops
digits = [0,1,2,3,4,5,6,7,8,9]

for i in range (len(digits)):
  print(digits[0:i])

print()
win_size = 2 #for bigger things
for i in range (len(digits)-win_size-1):#we minus one less than the window size
  print(digits[i:i+win_size])