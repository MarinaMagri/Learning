# d = {
#     key : value
# }

"""

a = ["Kharkov", "Kiev", "Poltava"]                                                           #-----list

d = {"Kharkov" : 57, "Kiev" :44, "Poltava" : 532}                                            #----dictionary
r = dict(Kharkov=57, Kiev=44, Poltava=532)                                                   #dictionary from "dict"
b = [["Kharkov", 57], ["Kiev", 44], ["Poltava",532]]                                         #dictionary from list
c = dict(b)
q = dict.fromkeys(["m", "y", "w"], 550)                                                      #dictionary from "fromkey"
v = {}                                                                                       # empty dictionary
w = dict()                                                                                   # empty dictionary too
print(w)
                                                                                             #The lists can't be a key([1,2,3] : 'two' --ERROR!)
del Dictionary_name[key]                                                                     # delete the dictionary                                             
b = {
    1 : 45,
    "hello" : "two",
    3 : [1, 2,3]
}
print(b["hello"])
b[12] = 18                                                                                   #add value to the dictionary
print(b)

for key in person:
    print(key, person[key])

d.clear()                                                                                    #clear all dictionary
d.get()                                                                                      #get key
d.get(4,"no such parameters")                                                                #add new key with parameter, if there isn't
d.setdefault(key(, parameter))                                                               #add new key without parameter, == // ==
d.pop(key)
d.popitem()                                                                                  #delete random key
d.keys()                                                                                     #get all keys in dictionary
d.values()                                                                                   #return all values
d.items()                                                                                    #return all pairs
sum(dic1.values())                                                                           #summ values in dictionary

for value in d.values:
    print(value)

for key, value in d.items:
    print(key, value)

"""

# person = {}
# s = "Ivanov Ivan Samara SGU 5 4 4 5 5 3 3 5"
# s = s.split()
# print(s)
# person["lastName"] = s[0]
# person["FirstName"] = s[1]
# person["City"] = s[2]
# person["University"] = s[3]
# person["Marks"] = s[4:]
# print(person)
# del person["Marks"]
# print(person)

# print(len(person))                                                                           #lenght
# print("lastName" in person, 5 in person, "contry" not in person)                             #Is there something?

# if "country" in person:
#     print(person["country"])
# else:
#     person["country"] = "United Kingdom"
#     print(person)

# s = input()
# d = {}
# for i in s:
#     if i.isalpha():
#         d[i] = d.get(i, 0) + 1
#         # if i in d:
#         #     d[i] += 1
#         # else:
#         #     d[i] = 1
# print(d)
# for i in sorted(d):
#     print(i, d[i])

# age = {"John" : 33, "Alex" : 37, "Ben" : 42}
# print(age)
# age["Dima"] = 12
# print(age)
# del age["Alex"]
# print(age)
# print(age["John"])
# print("Ben" in age)
# age2 = age.copy()
# print(age2)
# print(age.get("Dima"))
# print(age.items())
# print(age.keys())
# print(age.values())
# print(age.popitem())
# print(age)
# print(age2)
# age.update(age2)
# print(age)
# age3 = {"John" : 333, "Ben" : 45, 1 : False}
# age.update(age3)
# print(age)

# for key in age:
#     print(key, " - ", age[key])

# for key, value in age.items():
#     print(key, "-", value)

# dict = {0 : 10, 1 : 20}
# dict1 = {2 : 30} 
# dict.update(dict1) # dict.update({2 : 30})
# print(dict)

# dic1 = {1:10, 2:20}
# dic2 = {3:30, 4:40}
# dic3 = {5:50, 6:60}
# dic4 = {}
# print(dic4)

# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)

# for d in (dic1, dic2, dic3):
#     # print(f'd is {d}')
#     dic4.update(d)
#     print(dic4)


# dic1 = {1:10, 2:20}
# dic2 = {3:30, 4:40}
# dic3 = {5:50, 6:60}
# d = 2
# if d in dic1:
#     print("Done!")
# else:
#     print(f"There isn't {d} in the dictionary")

# dic1 = {1:10, 2:20}
# dic2 = {3:30, 4:40}
# dic3 = {5:50, 6:60}
# for dic in dic1,dic2,dic3:
#     print(dic)

# n = 1
# dict = {}
# for n in range(1,6):
#     dict.update({n: n*n})
# print(dict) 


# dict = {}
# for d in range(1,16):
#     dict[d] = d**2
# print(dict)

# dic1 = {"a":10, "b":20}
# dic2 = {"c":30, "d":40}
# dic1.update(dic2)
# print(dic1)

# dic1 = {"a":10, "b":20}
# dic2 = {"c":30, "d":40}
# dic3 = {"e":50, "f":60}
# e = {}
# for d in dic1,dic2,dic3:
#     e.update(dic1)
#     e.update(dic2)
#     e.update(dic3)
# print(e)

# dic1 = {"a":10, "b":20, "c":30, "d":40, "e":50, "f":60}
# print(sum(dic1.values()))


# dic1 = {"a":10, "b":20, "c":30, "d":40, "e":50, "f":60}
# print(multiply()


str = input("Enter your text ")
for x in str:
    if x not in "aeiou":
        print(x, end = " ")