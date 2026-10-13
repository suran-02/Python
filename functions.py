# square = lambda x:x**2
# print(square(78))
#
# add = lambda x,y,z:x+y+z
# print(add(23,89,71))
from traceback import print_tb

# check_age = lambda age: "Adult" if (age >= 18 and age < 100)  else "Minor"
# print(check_age(100))
#
# check_num = lambda num: "Even" if num%2==0 else "Odd"
# print(check_num(3190))
#
# greater = lambda x,y: x if x>y else y
# print(greater(90,50))
#
# last_char = lambda ch: ch[-1] if ch else None
# print(last_char(""))

students = [("Roy",85),("Alice",92),("Bob",78)]
print(sorted(students, key=lambda st:st[1]))

words = ["apple","cat","elephant","dog"]
print(sorted(words, key=len))