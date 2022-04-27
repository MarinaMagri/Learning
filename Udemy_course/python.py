from time import sleep
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



a = 5
b = 100
c = 0
d = 0
for x in range(a,b+1):
    if x % 3 == 0:
       c += x
       d += 1
print(c/d)

e = 6
f = 4

def nok(e,f):
    if e > f:
        answer = e
        while answer%f != 0:
            answer += e
    else:
        answer = f
        while answer%e != 0:
            answer += f
    print(answer)
