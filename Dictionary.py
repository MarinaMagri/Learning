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

age = {"John" : 33, "Alex" : 37, "Ben" : 42}
print(age)
age["Dima"] = 12
print(age)
del age["Alex"]
print(age)
print(age["John"])
print("Ben" in age)
age2 = age.copy()
print(age2)
print(age.get("Dima"))
print(age.items())
print(age.keys())
print(age.values())
print(age.popitem())
print(age)
print(age2)
age.update(age2)
print(age)
age3 = {"John" : 333, "Ben" : 45, 1 : False}
age.update(age3)
print(age)

for key in age:
    print(key, " - ", age[key])

for key, value in age.items():
    print(key, "-", value)