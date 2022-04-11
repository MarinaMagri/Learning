# list1 = [""]
# list2 = ["h", "c", "u", "m", "o", "s", "u", "o", "y", "e", "v", "o", "l"]
# z = -1
# for i in list2:
#     print(list2[z])
#     list1.append(list2[z])
#     z = z - 1


# print(list1)

# import re
# from t import printer
# printer()

# fruits = ["apple", "banana", "cherry"]
# print(fruits[1])

# cities = ("London", "Tokio", "New York")
# for city in cities:
#     print(city)

# a = ("text",)
# print(type(a))


# fruits = ("apple", "banana")

# (a, b) = fruits

# print(a)
# print(b)
# print(type(a))
# # print(red)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)

# print(type(red))


# list1 = [100, 200, 300, 400, 500]
# list1.reverse()
# print(list1)

# # num1 = int(input("Enter the first number"))
# # num2 = int(input("Enter the second number"))
# # if num1 >= num2:
# #     if num1 == num2:
# #         print(num1, "and", num2, "are equal")
# #     else:
# #         print(num1, "is greater then", num2)
# # else:
# #     print(num1, "is smaller then", num2)

# # num = float(input("Enter the number"))
# # if num >= 0:
# #     if num == 0:
# #         print(num, "is neutral")
# #     else:
# #         print(num, "is positive")
# # else:
# #     print(num, "is negative")


# num1 = int(input("Enter the first number:"))
# sign = input("Enter the sign:")
# num2 = int(input("Enter the second number:"))


# def summ(a, b):
#     return a+b


# def multiply(a, b):
#     return a*b


# def substruction(a, b):
#     return a-b


# def division(a, b):
#     return a/b


# if sign == "+": print(summ(num1, num2))
# elif sign == "-":
#     print(substruction(num1, num2))

# elif sign == "*":
#     print(multiply(num1, num2))

# else:
#     print(division(num1, num2))


# while True:
#     message = input("Enter your message:")

#     if message == "Hello" or message == "Hi":
#         print("Welcome!")
#     elif message == "How are you?" or message == "What's up?":
#         print("I'm OK!")
#     elif message == "Goodbye" or message == "Bye":
#         print("See you next time!")
#         break
#     else:
#         print("Please, try again!")

# print("END")


# name = input("Enter your name:")

# if name.lower() == "bond":
#     print("Welcome on board, 007")
# else :
#     print("Hello," + name)


# evens = 856596
# if evens % 2 == 0:
#     print(True)
# else:
#     print(False)

# 23/03/2022
# num = 333.4
# if type(num) == float :
#     print(num - int(num))
# elif type(num) == int:
#     print("Integer")
# else:
#     print('Please use numbers')
# elif num - int(num) == 0 :
#     print("Integer")


# exp = int(input("Please, enter your work experience:"))
# salary = int(input("Please, enter your salary:"))
# exp = 5
# def profit(salary):
#     print(salary + (salary*0.3))

# if exp >= 5:

#     profit(salary)
# else:
#     print("Sorry, there are no bonuses for you =(")


# length = int(input("Please, enter the length:"))
# weight = int(input("Please, enter the weight:"))

# if length == weight :
#     print("It's a square!")
# else:
#     print("Try again")


# a = input("Enter the first number:")
# b = input("Enter the second number:")
# if a > b :
#     print(a)
# elif a == b :
#     print("The numbers are equal")
# else :
#     print(b)

# amount = int(input("Enter your amount of goods:"))

# def total_cost():
#     return amount*100

# if total_cost() >= 1000:
#     print(total_cost() - (total_cost()*0.1))

# else:
#     print("Discount is missing")
# 24.03.2022
# grad =
# if grad <= 25:
#     print("You have got mark 'F'")
# elif grad >= 25 and grad < 45:
#     print("You have got mark 'E'")
# elif grad >= 45 and grad < 50:
#     print("You have got mark 'D'")
# elif grad >= 50 and grad < 60:
#     print("You have got mark 'C'")
# elif grad >= 60 and grad < 80:
#     print("You have got mark 'B'")
# else:
#     print("You have got mark 'A'")
#  p1 = 12 p2 = 56 p3 =45

# person1 = str(input("Enter your age:"))
# person2 = str(input("Enter your age:"))
# person3 = str(input("Enter your age:"))
# if person1 < person2 <person3:
#     print("person1 is youngest, person3 is oldest")
#     print(person1, "is youngest,", person3, "is oldest")
# elif person1 < person3 < person2:
#     print(2)
#     print(person1, "is youngest,", person2, "is oldest")
# elif person2 < person1 < person3:
#     print(3)
#     print(person2, "is youngest,", person3, "is oldest")
# elif person2 < person3 < person1:
#     print(4)
#     print(person2, "is youngest,", person1,"is oldest")
# elif person3 < person1 < person2:
#     print(5)
#     print(person3, "is younger,", person2, "is oldest")
# elif person3 < person2 < person1:
#     print(6)
#     print(person3, "is youngest,", person1, "is oldest")
# else:
#     print("all of them equal")


# classes = int(input("Number of classes held:"))
# attendance = int(input("Number of classes attended:"))
# medical_cause = input("Do you have medical cause?")
# def attend():
#     return((attendance/classes)*100)

# if attend() < 75:
#     print(attend(),"%", "Sorry, you didn't allowed for exams.")
# else:
#     if medical_cause.lower() == "yes":
#         print(attend(),"%", "Great! You attended for exams!")
#     else:
#         print("Sorry, you didn't allowed for exams.")


# year = 2083
# if year % 100 == 0:
#     if year % 400 == 0:
#         print("This year is leap")
#     else:
#         print("This year isn't leap")
# elif year % 4 == 0:
#     print("This year is leap")
# else:
#     print("This year isn't leap")

# 25/03/2022
# def t():
#     6 + 6


# age = int(input("Enter your age:"))
# sex = input("Enter your sex (M or F):")
# if sex.lower() == "f":
#     "You will work in urban areas"
# elif sex.lower() == "m":
#     if age >= 20 and age < 40:
#         print("You may work in anywere")
#     elif age >= 40 and age < 60:
#         print("You may work in urban areas only")
#     else:
#         print("Error")
# else:
#     print('Wrong sex')



# def my_func(x: int, y: int):
#     8*8
#     s = 't'
#     x = 'f'
#     t = 'hello'
#     print(y)
#     print('my code')
#     return t+x+t

# r = 9
# print('text {r}')




# print(t())

# def greet(name):
#     # print(f'Hi {name}')
#     return '...'

# print(greet('Mosh'))


# a = ['fjdlsssl','u']
# c = ('fjdlsssl','u')
# b = 'gygyygyg'
# b = b + 'jjjj'
# b = 666

# def y():
#     print("Text GGGGG")

# d = (7,)
# z = [7, y(), ['a']]
# print(type(c))
# print(z)
                                                                                      # 29/03/22
# colours = ["blue","green","red","yellow"]
# fruits = ["blueberry","apple","cherry","banana"]
# print(colours[1],fruits[1])
# print(colours[0],fruits[0])
# print(colours[2],fruits[2])



# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# a = [list1[0] + list2[0], list1[1] + list2[1], list1[2] + list2[2], list1[3] + list2[3]]

# print(a)

# numbers = [1, 2, 3, 4, 5, 6, 7]
# print(numbers*2)

# print(zip(list1, list2))

# numbers = [5, 2, 7]
# numbers.append(100)
# numbers.insert(1, True)
# b = [5, 4, 3]
# numbers.extend(b)
# numbers.sort()
# numbers.reverse()
# a = numbers.pop()
# # numbers.remove()/
# numbers.pop(4)
# print(numbers.count(5))
# print(len(numbers))

# # print(numbers)

# n = int(input("amount of numbers:"))
# sum_x = 0.0
# for i in range(n):
#     sum_x += float(input())
# print("Average", sum_x / n)

# list1 = ["Oliver", "Harry", "Jack", "Leo", "Charlie"]
# print(list(enumerate(list1)))

# list2 = ["Oliver", "Harry","Jack", "Leo", "Charlie"]
# for index, value in enumerate(list2):
#     print(index, value)

# persons = ["Smith","Jones", "Taylor", "Brown", "Williams", "Williams"]
# sub_str = input("Look for:")    

# for i, p in enumerate(persons):
#     if p.count(sub_str) !=0:
#         print("Found", p, i , "position in the queue")


# i = 1
# while i <= 10:
#     print(i)
#     i += 1


# i = 1
# while i <= 5:
#     print(i, i+1)
#     i +=1

# qee = 1
# print(qee)
# letters = 'ABCDEFGHIJ'
# numbers = '0123456789'
# import string
# for letter in letters:
#     #print(letter)
#     for number in 'numbers':
#         #print(f'{letter}{number}')
#         for HER_SOBACHIY in 'qazty':
#             qee+=1
#             print(number)

# var = 10
# for i in range(10):
#     # for j in range(2, 10, 1):
#     #     if var % 2 == 0:
#     #         continue
#     #         var += 1
#     var+=1
# else:
#     var+=1
# print(var)


# count = 0
# for i in ['abcdef','dfefef','fefefe']:
#     count = count + 1
#     if count > 2:
#         break
#     else:
#         print(i)
# else:
#     print("Done")

# str = "ello! I'm m ine"
# str_tmp = ''
# helper1 = 'union'
# helper2 = 'K'
# helper3 = 'marked'
# helper4 = 'h'
# helper5 = 'frockless'

# DO SOME MAGIc HERE

# print(str) # This should looks as follows: "Hello! I'm from Ukraine!"
# print(helper5[:3] + str[10])
# print(helper4)
# print(helper4 + str)
# str = helper4.capitalize() + str[:10] + helper5[:3] + str[10] + " " \
#         + helper1[0].capitalize() + helper2.casefold() + helper3[2] + helper3[1] + str[-3:] + str[4]
# print(str)

# for j in range(1,11):
#     print(f"7*{j} = {j*7}")
#     print("7*" + str(j) + " = " + str(j*7))


# rows = 12
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end= " ")
    # print('')


# rows = 5
# b = 0
# for i in range(rows, 0, -1):
#     b += 1
#     for j in range(1, i + 1):
#         print(b, end= "")
#     print('\r') #

#     a = ["a"]
#     for i in a:
#         print(a)
#         a.append("a") 
# "hello world".replace("l", " ")

'''
1. For: use loop for to print the following matrix:
a5 b5 c5 d5 e5
a4 b4 c4 d4 e4
a3 b3 c3 d3 e3
a2 b2 c2 d2 e2
a1 b1 c1 d1 e1

2. List: assign the following string:
s = "This X my favorite books"
turn it to a list, update X to a correct world
turn it back to a string

3. While: create a user input that asks for a variable. Validate that this variable is in range between 1 and 3.
Create a while loop that uses variable from an input above. Print any text within a loop and use a timout for 1 second.

4. Create a user input that asks a user for 'Y' or 'N'. Accept letters in any case. 
Create indefinite loop while answer is wrong.
'''  
# for while list time out matrix 


# for a in range(5, 0, -1):
#     for i in str("abcde"):
#         print(f"{i}{a}", end =" ")
#     print()

# s = "This X my favorite books" 
# l = s.split()
# l[0] = "These" 
# l[1] = "are"
# s = " ".join(l)
# print(s)


# import time

# i = int(input("Enter your variable:"))
# if i>=1 and i<=3:
#     while i in range(1,3):
#         i += 1
#         time.sleep(1)
#     print("ok")
# else:
#     print("Try again")

# a = ""
# while a.lower() != "y" and a.lower() != "n":
# while a.lower() not in "yn":


# while a.lower() not in 'yn':
#     a = input("Are you a woman? (y/n)") 

'''
1. Create a user input that asks a user for 'Y' or 'N'. Accept letters in any case. 
Create indefinite loop while answer is wrong.
Use IF and Functions. Do not use WHILE

2. Here is the tuple:
t = ('Maria','Pavel','Max','Siri','Cockroach','Monika')
You should implement the functionality so the script checks all the names, and remove the name if it contains 'i' letter. 
The following command should print correct answer and it should be tuple:

if type(t) == tuple: print(f'PASS: {t}')

'''

# def get_value():
#     a = input("Please enter the value (y/n:)")
#     # if a != 'y' and a != 'n':
#     if a.lower() != "y" and a.lower() != "n":
#         print(a)
#         get_value()
#     else:
#         print("Well done!")

# get_value()

'''
1. Here are two strings, check if they contain the following letters: a, c, w, z
s1 = "This is my favorite castle. The princess lives there."
s2 = "In tech we trust"


2. Here is the tuple:
t = ('Maria','Pavel','Max','Siri','Cockroach','Monika')
You should implement the functionality so the script checks all the names, and remove the name if it contains 'i' letter. 
The following command should print correct answer and it should be tuple:

if type(t) == tuple: print(f'PASS: {t}')
'''

# t = ('Maria','Pavel','Max','Siri','Cockroach','Monika')
# l = list(t)
# for a in l:
#     if "i" in a:      # if "i" in "Maria"
#         l.remove(a)
# t = tuple(l)
# print(t)

# if type(t) == tuple: print(f'PASS: {t}')




# 1. Here are two strings, check if they contain the following letters: a, c, w, z
# s1 = "This is my favorite castle. The princess lives there."
# s2 = "In tech we trust"
# count all occurencies and print them in the following view:
# s1 -- a:X c:Y w:Z z:A
# where are X,Y,Z,A times when you encounter needed letter
# print where more encounters is with total encounters

s1 = "This is my favorite castle. The princess lives there."
s2 = "In tech we trust"

print("a:" + str(s1.count("a")) + ", c:" + str(s1.count("c")) + ", w:" + str(s1.count("w")) + ", z:" + str(s1.count("z")))
print(f'a:{s1.count("a")}, c:{s1.count("c")} w:{s1.count("w")}, z:{s1.count("z")}')
print("a:" + str(s2.count("a")) + ", c:" + str(s2.count("c")) + ", w:" + str(s2.count("w")) + ", z:" + str(s2.count("z")))

sum1 = s1.count("a") + s1.count("c") + s1.count("w") + s1.count("z")
sum2 = s2.count("a") + s2.count("c") + s2.count("w") + s2.count("z")
print("Total in s1:", sum1, ", total in s2:", sum2)
print(f"Total in s1: {sum1}, total in s2: {sum2}.")

if sum1 > sum2:
    print("S1 has more letters")
if sum1 < sum2:
    print("S2 has more letters")


i = 5
"We have: " + str(i) + " cows. And a is " + str(s2.count("a"))
#"We have 5 cows"
f'We have: {i} cows. And a is {s2.count("a")}'