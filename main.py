import turtle
# square
pratik_turtle = turtle.Turtle()
pratik_turtle.speed(7)


def square():  #we define a function here

    pratik_turtle.forward(100)
    pratik_turtle.right(90)
    pratik_turtle.forward(100)
    pratik_turtle.right(90)
    pratik_turtle.forward(100)
    pratik_turtle.right(90)
    pratik_turtle.forward(100)


square()  #now above large code is stored in it now
print()

import calendar
#used to output days in week
print(calendar.weekheader(3))
print()  #using another one to find mon as 0
print(calendar.firstweekday())
print()
# using this to find out the month via year and date
print(calendar.month(2022, 9))
print()  #in matrix formation of above
print(calendar.monthcalendar(2022, 9))
print()  #printing the whole fucking year 2022
print(calendar.calendar(2022))
print()  #printing the no of the week day
day_of_the_week = calendar.weekday(2022, 8, 9)
print(day_of_the_week)
print()  #finding whearher a year is a leap year or not
is_leap = calendar.isleap(2020)
print(is_leap)
print()
how_many_leap_days = calendar.leapdays(2000, 2023)
print(how_many_leap_days)
print()

elephant_weight = 200
ant_weight = 2

if elephant_weight > ant_weight:
    square()
else:
    pratik_turtle.forward(100)
    print('holla')
    #while loop done
    #for loop indentation problem

#datatypes adn casting(to change one datatype to another )
  #integers
  #1,3,4
  #floats
  #2.44
  #strings
  #"3"
  #boolens
#yes or no /true or False
print()

#learning about strings
print()
s="happy coder"
print(s)
print()

#printing inside string i,e single words ex
print(s[0])
print()

#learning lists

l = [1,2,3]
print (l[1])
print()

#complex lists
list2 =["string" ,'singel', True,4.2,[1,2,3]]
print(list2[0])
print(list2[1])
print(list2[2])
print(list2[3])
print(list2[4])
print()
#append in lists (puting something at the end of the list
