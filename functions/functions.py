
#intro to functions
#creating a function

def pritnStuff(myMsg):
    print(myMsg)

def greetings(name):
    print(f"Hi! My name is {name}")

greetings("Iveta")

#typeInt



#default args/parameters

def calc(a = 2, b = 2): #now you can call without variables, you can overwrite py adding them
    print(a + b)
    print(a - b)
    print(a % b)
    print(a * b)
    print(a / b)

num1 = int(input("enter first num"))
num2 = int(input("enter second num"))

calc(num1, num2)


#multiple args - accepts any amount of args

# def multiArgs(*multiargs):
#     print(type(multiargs))
#
#     for arg in multiargs:
#         print(arg)
#
# multiArgs(1,2, 3, 4, 5)

