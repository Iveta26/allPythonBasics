
#unordered and will not print in the order as its input,
#no indexes

car_parts = {"wheels", "windows", "exhaust", "steering wheel"}

print(car_parts)

#add to a set

car_parts.add("doors")
print(car_parts)

car_parts.remove("windows")

print(car_parts)


#frozen set
#imutable set
#this is so ugly
#built in function
x = frozenset(["two", "one", "three", "four"]) # a list wrapped in a frozen set

print(x)