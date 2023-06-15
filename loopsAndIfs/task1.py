

print("Please enter your age")
flag = True

while flag:
    try:
        age = int(input())
    except ValueError:
        print("Please enter numerical value")
    else:
        if int(age) > 117 or int(age) <=0:
            print(f"The age {age} isn't valid")
        else:
            if age >= 18:
                print("You can watch all movies")
                flag = False
            elif age >= 16:
                print("Sorry you cannot watch 18 rated movies, but you can watch all the other movies")
                flag = False
            elif age >= 13:
                print("Sorry you cannot watch 18 or 15 rated movies, but you can watch all the other movies")
                flag = False
            elif age >= 8:
                print("Sorry you cannot watch 18 or 15 or 12 rated movies, but you can watch all the other movies")
                flag = False
            else:
                print("You can only watch U rated movies")
                flag = False


