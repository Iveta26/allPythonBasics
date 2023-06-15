
#input = int(input("Please enter a number 1-100"))
number = 1

if input % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")


while number <101:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)
    number += 1