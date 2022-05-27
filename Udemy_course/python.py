# name = input("Enter your name: ")
# if name == "Victor":
#     print("Such user already exists")
# elif name == "Denis":
#     print("You are an autor of course")
# else:
#     print("ok")

# a = int(input())

# if a > 10:
#     print("More than 10")
# else:
#     print("Less or equal 10")

# if a >10 and a < 20:
#     print("Interval is correct")
# else:
#     print("Other")

# if a > 30 or a < 20:
#     print("Ok")
# else:
#     print("Other")

# if not a > 5:
#     print("Less than 5")
# else:
#     print("More than 5")
                                        #Task #1 "if,elif,else"
# a = 7 #не менее
# b = 9 #не более
# c = 2 #спит
# if c >= a and c <= b:
#     print("У вас все хорошо со сном")
# elif c < a:
#     print("У вас недосып!")
# else:
#     print("У вас пересып")
                                        #Task #2 (loop 'for')
# a = 5
# b = 100
# c = 0
# d = 0
# for x in range(a,b+1):
#     if x % 3 == 0:
#        c += x
#        d += 1
# print(c/d)
                                        #Task #2 (loop 'While')
# e = 6
# f = 4

# def nok(e,f):
#     if e > f:
#         answer = e
    #     while answer%f != 0:
    #         answer += e
    # else:
    #     answer = f
    #     while answer%e != 0:
    #         answer += f
    # print(answer)

'''
LISTS
'''
# l=[]
# l.append("element")                    #add the new element to the list
# l.pop()                                #delete the last element on the list
# l.count("element")                     #count the element
# l.sort()                               #sort the elements
# l.reverse()                            #revers the elements

# def num(a,b):
#     l = []
#     for i in range(a,b+1):
#         if "5" not in str(i):
#             l.append(i)
#             print(l)
#     print(len(l))


'''
DICTIONARIES
'''
# d = {}
# d["key"] = Value                       #add new key to the dictionary
# d["name"]                              #call to the key
# "name" (not) in d:                     #is there "name" on dictionary
# d.get("key")                           #get value of the key
# del d["key"]                           #delete pair of key:value
# for key in d (d.keys):                 #enumeration of keys
# for value in d:                        #enumeration of values
# for key in d: print(d[key])            #print the values
'''
tuple
'''
# a = ()


'''
SETS
'''
# first_set = {"Alex", "Bob", "John", "Andrey"}
# second_set = {"Don", "Andrey", "Tom", "Bob", "John"}
# third_set = first_set.union(second_set)

# repeat_elems = first_set.intersection(second_set)
# diff_element = second_set.difference(first_set)
# print(diff_element)

# a = {}                                  #Its NOT set, its DICTIONARY        
'''
FUNCTIONS
'''
# def name_func(arguments)
# def plus(a,b):
#     return a + b
# plus(2,2)

# def func(*args):
#     for arg in args:
#         print(arg)

# func(2,3,4,5,6)

# def func(**kwargs):                     #Kwargs=dictionary
#     for key in kwargs:
#         print(key, kwargs[key])

# func(name = "Denis", number = 10, status=True)

# def add(a,b):
#     return a + b

# print(add(b=4, a=2))

# def func(a = 10, b = 20):
#     return a + b

# print(func())

                                           #Task #3 (Function)
# def function(x):
#     if x <=-2:
#         return(1 - (x + 2)**2)
#     elif x > -2 and x <= 2:
#         return(-(x/2))
#     elif x > 2:
#         return((x - 2)**2 + 1)

# print(function(-4.5))
# print(function(4.5))
# print(function(1))
'''
LAMBDA
'''

# is_adult = lambda age: age >= 18
# print(is_adult(25))

# plus = lambda a,b: a + b
# print(plus(5,10))

# tr = lambda: True
# print(tr())
'''
EXEPTIONS, ERRORS
'''
# try:
#     print(1/0)
# except ZeroDivisionError: 
#     print("You can't division by 0")

# try:
#     print("Hello")
# except Exception as error:
#     print(f"Error is {error}")
# else:
#     print("There aren't errors")
# finally:
#     print("End")

'''
Modules, PIP
'''

'''
OOP
''' 
# class Comment:                               #Create class 'Comment'
#     def __init__(self, author, text):
#         self.author = author
#         self.text = text

#     def showText(self):
#         print(f"Текст комментария: {self.text}")


# comment = Comment("Denis", "Text comment")   #transfer 'Denis' in author and 'Text comment' in text
# print(comment.text)
# comment.text = "New text"                    # changed value of text
# print(comment.text)

# other_comment = Comment("Alex", "Other text")
# print(other_comment.text)
# comment.showText()


# class Car:
#     def __init__(self, brand, model, year, mileage):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.mileage = mileage 

#     def showCar(self):
#         print(f"Машина -> brand: {self.brand}, модель: {self.model}, год выпуска: {self.year}, пробег: {self.mileage}")

#     def driveCar(self, km):
#         self.mileage += km

# chaser = Car("Toyota", "Chaser", 1998, 200000)
# chaser.showCar()
# chaser.driveCar(100)
# chaser.showCar()


# class ElectroCar(Car):
#     def __init__(self,brand, model, year, mileage):
#         super().__init__(brand, model, year, mileage)
#         self.battary = 100
    
#     def ShowBattaryInfo(self):
#         print(f"Заряд батареи: {self.battary}%")

# Tesla = ElectroCar("Tesla", "Model X", 2016, 10000)
# Tesla.ShowBattaryInfo()
# Tesla.driveCar(150)
# Tesla.showCar()

#                                     # _ - protected, __ - private
# class VkAccount():
#     def __init__(self, login, password):
#         self._login = login
#         self.__password = password

#     def signIn(self):
#         if self._login == "admin" and self.__password == "12345":
#             print("Succesful!") 
#         else:
#             print("Wrong Data!")

# my_account = VkAccount("admin", "12345")
# my_account.signIn()
# # print(my_account.__password)
# print(type(my_account))
# my_account._login = 'not_admin'

# print(my_account._login)


# class MyClass():
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         # return self.name
#         return f"-> {self.name}"


# abc = MyClass("Yuriy")
# print(abc)


# class MathModule:
#     def __init__(self):
#         pass

#     def Square(self, n):
#         return n**2
    
#     def Cub(self, n):
#         return n**3

#     def is_positive(self, n):
#         if n > 0:
#             return "It's Positive"
#         else:
#             return "Less or equal 0"

#     def is_negative(self, n):
#         if n < 0:
#             return "Negative"
#         else:
#             return "More or equal 0"

#     def S(self, l, w):
#         return l * w

#     def P(self, l, w):
#         return (l + w) * 2 

#     def __str__(self):
#         return "Math Module"


# module = MathModule()

# print(module.Square(3))
# print(module.Cub(3))
# print(module.is_positive(123))
# print(module.is_positive(-123))
# print(module.is_negative(-325))
# print(module.is_negative(698))
# print(module.S(5,10))
# print(module.P(25,3))

'''
WORKING WITH FILES
'''


# f = open("text.txt", "r")

# s = f.readlines()

# for line in s:
#     line.strip()
#     print(line)

# f.close()


# with open("text.txt", "r", encoding="utf8") as f:           #after this method File closed automatically
#     s = f.readlines()
#     for line in s:
#         line.strip()
#         print(line)


# with open("text.txt", "r", encoding = "utf8") as f:
#     for line in f:
#         line.strip()
#         print(line)



# with open("output.txt","w", encoding = "utf8") as f:
#     f.write(f"Working with Files\n")

# # with open("output.txt","w", encoding = "utf8") as e:
#     for i in range(11):
#         f.write(f"{i}\n")


# def is_square(n):  
#     n**0.5 == float(0):
#         return True
#     else:
#         return False

# print(is_square(25))

# print(25**0.5)
