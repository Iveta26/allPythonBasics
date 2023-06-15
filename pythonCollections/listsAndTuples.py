#lists and tuples


#making a list in python

shoppingList = ["eggs", "bread", "cheese", "haggis"]

print(shoppingList)


breadPop = shoppingList.pop(1)

print(shoppingList)

shoppingList.remove("eggs")

shoppingList.append("butter")
print(shoppingList)

print("this is my pop val: " + breadPop)


#list slicing
shoppingList = ["eggs", "bread", "cheese", "haggis"]
print(shoppingList[1:3])

print(shoppingList[::2]) #every second step skipped over


#Tuples
# () - immutable, cannot be changed

essentials = ("bread", "eggs", "milk")
print(essentials)

print(essentials.count("bread"))
