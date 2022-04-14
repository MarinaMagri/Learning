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

"""

person = {}
s = "Ivanov Ivan Samara SGU 5 4 4 5 5 3 3 5"
s = s.split()
print(s)
person["lastName"] = s[0]
person["FirstName"] = s[1]
person["City"] = s[2]
person["University"] = s[3]
person["Marks"] = s[4:]
print(person)
del person["Marks"]
print(person)

