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
                                            # exercice 1 "if,elif,else"
# a = int(input("Рекомендации по сну: "))
# b = int(input("Нужно спать не более: "))
# c = int(input("Введите количество чвсов вашего сна: "))
# if c == a:
#     print("У вас все хорошо со сном")
# elif c < a:
#     print("У вас недосып!")
# else:
#     print("У вас пересып")

# a = 5
# b = 100
# c = 0
# d = 0
# for x in range(a,b+1):
#     if x % 3 == 0:
#        c += x
#        d += 1
# print(c/d)

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

# a = {}                                    #Its NOT set, its DICTIONARY        
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

# def func(**kwargs):                                #Kwargs=dictionary
#     for key in kwargs:
#         print(key, kwargs[key])

# func(name = "Denis", number = 10, status=True)

# def add(a,b):
#     return a + b

# print(add(b=4, a=2))

# def func(a = 10, b = 20):
#     return a + b

# print(func())

